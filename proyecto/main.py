import requests
import csv
import datetime

# Tu clave de API de OpenWeatherMap
API_KEY = 'a5b95fa1d7a206a105f9d6d831ee267c'

# Ciudad para la que deseas obtener datos meteorologicos
CIUDAD = 'Bogota'

# URL base de la API de OpenWeatherMap
URL_BASE = "http://api.openweathermap.org/data/2.5/weather?"

def obtener_datos_clima(ciudad):
    """Obtiene los datos meteorológicos de una ciudad dada.

    Args:
        ciudad (str): Nombre de la ciudad.

    Returns:
        dict: Un diccionario con los datos meteorológicos, o None en caso de error.
    """
    print(f"Obteniendo datos meteorológicos para {ciudad}...")
    url_completa = URL_BASE + "appid=" + API_KEY + "&q=" + ciudad
    respuesta = requests.get(url_completa)

    if respuesta.status_code == 200:
        print("Datos obtenidos exitosamente.")
        return respuesta.json()
    else:
        print(f"Error al obtener datos meteorológicos para {ciudad}: {respuesta.status_code}")
        return None

def guardar_en_csv(datos, ciudad):
    """Guarda los datos meteorológicos en un archivo CSV.

    Args:
        datos (dict): Diccionario con los datos meteorológicos.
        ciudad (str): Nombre de la ciudad.
    """
    if datos:
        print("Guardando datos en CSV...")
        # Extrae los datos relevantes del diccionario, incluyendo lluvia y nieve
        temperatura = datos["main"]["temp"]
        humedad = datos["main"]["humidity"]
        descripcion = datos["weather"][0]["description"]
        lluvia = datos.get("rain", {}).get("1h", 0)  # Maneja la ausencia de datos de lluvia
        nieve = datos.get("snow", {}).get("1h", 0)  # Maneja la ausencia de datos de nieve

        nombre_archivo = f"/home/sebastianmorales/proyecto/clima_{ciudad.lower()}_{datetime.date.today()}.csv"
        with open(nombre_archivo, mode='a', newline='') as archivo:
            escritor = csv.writer(archivo)
            # Escribe el encabezado solo si el archivo está vacío
            if archivo.tell() == 0:
                escritor.writerow(["Fecha", "Ciudad", "Temperatura (K)", "Humedad (%)", "Descripción", "Lluvia (mm)", "Nieve (mm)"])
            escritor.writerow([datetime.datetime.now(), ciudad, temperatura, humedad, descripcion, lluvia, nieve])
        print("Datos guardados exitosamente.")
    else:
        print("No se pudieron guardar los datos.")

try:
    # Obtener los datos meteorológicos
    print("Iniciando obtención de datos...")
    datos_clima = obtener_datos_clima(CIUDAD)
    # Guardar los datos en un archivo CSV
    guardar_en_csv(datos_clima, CIUDAD)
    print("Proceso completado.")
except Exception as e:
    print(f"Se produjo un error: {e}")
