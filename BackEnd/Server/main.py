from flask import Flask
from flask import jsonify
from flask import request, send_file
from flask_cors import CORS
#import utils.values as values
import utils.queries as queries
import utils.collage as collage
import time

main = Flask(__name__)
main.config["DEBUG"] = True
cors = CORS(main)
#main.config["CORS_HEADERS"] = "Content-Type"

# Contains an example of a get method
@main.route("/get/sample", methods=["GET"])
def GetSample():
    return "Get method"


@main.route('/home/getPhoto', methods=['GET'])
def GetPhoto():
    
    #limpio la carpeta
    
    if(queries.checkDistance()):

        collage.clean()

        for _ in range(6):
            print("Tomo foto")
            queries.TakePhoto()
            time.sleep(1)

        path = collage.createCollageMulti()

        #Tomo las fotos
        collage.clean()

        for _ in range(6):
            print("Tomo foto")
            queries.TakePhoto()
            time.sleep(1)

        path = collage.createCollage()

        # return str(path)
        
        ###envia el archivo
        return send_file(path)
    
    else:
        return jsonify("Se necesita acercar o alejar del sensor"), 404




        
if __name__ == '__main__':
    #main.run(host=values.host, port=values.port)
    try:
        queries.start_flag_sensor()
        main.run(host="0.0.0.0", port=5000)
    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        queries.finish_flag_sensor()