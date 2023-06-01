from utils.libGPIO import *
import utils.values as values
import os
import datetime

##Agregar la parte del sensor

def TakePhoto():
    image_name = f'/Server/src/{datetime.datetime.now()}.jpg'.replace(' ', '_')
    os.system(f'fswebcam --no-banner {image_name}')
    return image_name