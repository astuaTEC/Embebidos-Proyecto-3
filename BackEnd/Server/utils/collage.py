from PIL import Image, ImageDraw
import os, shutil
import time
from joblib import Parallel, delayed
# Ruta al directorio que contiene las imágenes
directory = "./src/"


# Dimensiones del collage
collage_width = 320
collage_height = 960


# Función para procesar cada imagen y colocarla en el collage
def process_image(image_file):
    try:
        image_path = os.path.join(directory, image_file)
        image = Image.open(image_path)

        # Redimensionar la imagen para que se ajuste al tamaño del collage
        image = image.resize((320, 160))

        # Crear una nueva imagen en blanco para la imagen actual
        image_canvas = Image.new("RGB", (320, 160), (255, 255, 255))

        # Copiar la imagen en blanco en la nueva imagen
        image_canvas.paste(image)
        #image_canvas.save(f"collage{image_file}.jpg")
        

        #print(f"Procesada imagen: {image_file}")

        return image_canvas

    except Exception as e:
        #print(f"Error al procesar imagen: {image_file} - {str(e)}")
        return None

def createCollage():
    # Obtener la lista de archivos de imagen en el directorio
    files = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.jpeg', '.png'))]
    print("-----------------------------------------------------")
    print("Creando Collage sin paralelismo:")
    start_time = time.time()

    result_images = []

    # Procesar cada imagen en un ciclo for
    for image_file in files:
        result_image = process_image(image_file)
        result_images.append(result_image)

    # Crear una nueva imagen en blanco para el collage final
    final_collage = Image.new("RGB", (collage_width, collage_height), (255, 255, 255))
    n = 0
    # Combinar todas las imágenes procesadas en el collage final
    for image in result_images:
        if image is not None:

            # Calcular las coordenadas para colocar la imagen en el collage
            if n == 0:
                x=0
                y=0
                n = 1      

            # Colocar la imagen en la nueva imagen
            final_collage.paste(image,(x, y))

            #x += image.width
            y += image.height

    # Guardar el collage resultante
    final_collage.save("/Server/image/collage.jpg")

    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"Tiempo total de procesamiento: {total_time} segundos")
    print("-----------------------------------------------------")
    return "/Server/image/collage.jpg"




def createCollageMulti():

    # Obtener la lista de archivos de imagen en el directorio
    files = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.jpeg', '.png'))]
    print("-----------------------------------------------------")
    print("Creando Collage con paralelismo:")


    start_time = time.time()
    final_collage = Image.new("RGB", (collage_width, collage_height), (255, 255, 255))
    # Obtener el número de núcleos del procesador
    result_images = []
    n = 0
    # Iniciar el proceso paralelo para el collage utilizando multiprocessing
    result_images = Parallel(n_jobs=-1)(delayed(process_image)(image_file) for image_file in files)
    
        # Combinar todas las imágenes procesadas en el collage final
    for image in result_images:
        if image is not None:
            # Calcular las coordenadas para colocar la imagen en el collage
            if n == 0:
                x=0
                y=0
                n = 1      

                # Colocar la imagen en la nueva imagen
            final_collage.paste(image,(x, y))

                #x += image.width
            y += image.height
    # Crear una nueva imagen en blanco para el collage final
    
    
    
    

    # Guardar el collage resultante
    final_collage.save("/Server/image/collage.jpg")

    end_time = time.time()
    total_time = end_time - start_time

    print(f"Tiempo total de procesamiento: {total_time} segundos")
    print("-----------------------------------------------------")
    return "/Server/image/collage.jpg"


def clean():
        
    #folder = '/Users/GabuRolo/Documents/Progras/embebidos/P3/Embebidos-Proyecto-3/BackEnd/Server/image'
    
    
    #Para que elimine las imagenes viejas
    folder = "./src/"
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))