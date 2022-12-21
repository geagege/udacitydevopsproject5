from flask import Flask
 
app = Flask(__name__)
 
@app.route("/hello", methods=["GET"])
def hello():
    return 'Hello World. My name is Sonhh9'

@app.route("/", methods=["GET"])
def home():
    return 'Hello World. My name is Sonhh9'
 
app.run(host="0.0.0.0", port=80, debug=True)