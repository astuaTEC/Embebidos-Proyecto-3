from utils.libGPIO import *
import utils.values as values
import os
import datetime

##Agregar la parte del sensor
FLAG_PIN = 21

def TakePhoto():
    image_name = f'/Server/src/{datetime.datetime.now()}.jpg'.replace(' ', '_')
    os.system(f'fswebcam --no-banner {image_name}')
    return image_name

def start_flag_sensor():
    if export_command(FLAG_PIN) == values.error:
        print(f"Sensor Error: Pin {FLAG_PIN} for flag failed to start.")
    else:
        if pin_mode(FLAG_PIN, values.iMode) == values.error:  # Corregido: Usar values.iMode para pin de echo
            print(f"Sensor Error: Pin {FLAG_PIN} for flag failed to start.")

def finish_flag_sensor():
    unexport_command(FLAG_PIN)

def checkDistance():
    res = digital_read(FLAG_PIN)
    return True if res == 1 else False