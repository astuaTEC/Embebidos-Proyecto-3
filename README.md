# Proyecto 3 - Fotomatón

## Breve descripción de la propuesta
Crear un fotomatón utilizando una cámara conectada a una Raspberry Pi 2 para tomar varias fotografías seguidas y combinarlas en una única imagen personalizada y divertida. La aplicación se mejorará utilizando técnicas de procesamiento de imágenes con la biblioteca "Pillow" y OpenMP para aprovechar el rendimiento de sistemas multi-core. Además, se incluirá un sensor ultrasónico para activar la captura de imágenes a una cierta distancia y una aplicación web para visualizar los resultados y controlar el fotomatón.

## Instrucciones para su uso

1. Introducir la tarjeta de memoria en la RPi 2.
2. Conectar los periféricos necesarios (teclado, monitor, cámara, ...)
3. Conectar a la corriente la RPi 2. Poner como contraseña "root".
4. Asegurarse de estar conectado a Internet. Para ello ejecute el comando `ifconfig`. (Anote la IP)
5. Navegar a la carpeta `/Server`.
6. Ejecutar el comando `python3 main.py`.

Del lado del FrontEnd:
1. Abrir el código fuente de FrontEnd (`cd FronEnd`)
2. Ejecutar el comando `yarn install`
3. Modificar el archivo `.env` con la URL que tiene la RPi 2.
4. Ejecutar el comando `yarn dev`