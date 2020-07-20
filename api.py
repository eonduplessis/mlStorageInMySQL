from flask import request, Flask
from werkzeug.exceptions import HTTPException
from dbconnect import fetch_model_data

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/getModel', methods=['GET'])
def get(modelName: str):
    if request.headers["Content-Type"] != 'application/json':
        raise HTTPException(400, "Request should be in application/json format!")
    return {
        "data":
            {
                'modelData': fetch_model_data(modelName)
            }
    }