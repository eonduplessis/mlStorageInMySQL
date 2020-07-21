from flask import request, Flask, send_file
from werkzeug.exceptions import HTTPException
from dbconnect import fetch_model_data, write_model_data
import io

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/getModel/<modelName>', methods=['GET'])
def getModel(modelName):
    return send_file(io.BytesIO(fetch_model_data(modelName)),
                     attachment_filename='val.jpeg',
                     mimetype='image/jpg')
           


@app.route('/postModel/<modelName>', methods=['POST'])
def updateModel(modelName):
    file = request.files['file']
    write_model_data(modelName, file)

app.run()