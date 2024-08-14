#!/bin/bash
echo "Script started at $(date)" >> /home/sebastianmorales/proyecto/debug.log
/home/sebastianmorales/miniforge3/bin/python3 /home/sebastianmorales/proyecto/main.py >> /home/sebastianmorales/proyecto/debug.log 2>&1
echo "Script ended at $(date)" >> /home/sebastianmorales/proyecto/debug.log



