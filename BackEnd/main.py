from flask import Flask
from flask import jsonify
from flask import request, send_file
from flask_cors import CORS
#import utils.values as values
#import utils.queries as queries
import utils.collage as collage

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
    

    #Tomo las fotos

    for _ in range(5):
        print("Tomo foto")
        #queries.TakePhoto()


    #img_path1 = queries.TakePhoto()
    #img_path2 = queries.TakePhoto()
    #img_path3 = queries.TakePhoto()
    collage.clean()
    path = collage.createCollage()
    collage.clean()
    path = collage.createCollageMulti()
    return str(path)
    
    
    ###envia el archivo
    #return send_file(path)




        
if __name__ == '__main__':
   #main.run(host=values.host, port=values.port)
   main.run(host="0.0.0.0", port=5000)