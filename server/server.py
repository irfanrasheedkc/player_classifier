from flask import Flask , request , jsonify
import util
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/hi')
def hi():
    return "hi"

@app.route('/classify_image',methods=['GET' , 'POST'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))
    response.headers.add('Access-Control-Allow-Origin' , '+')

    return response
if __name__ == "__main__":
    print("Starting Python Flask Server For Sports Celebrity Image Classification")
    util.load_saved_artifacts()
    print("Loading completed")

    app.run(port=5000)