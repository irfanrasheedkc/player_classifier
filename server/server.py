from flask import Flask
import util
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/classify_image',methods=['GET' , 'POST'])
def classify_image():
    pass

if __name__ == "__main__":
    app.run()