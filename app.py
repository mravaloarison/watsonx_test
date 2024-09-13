from flask import Flask
from assistant import watsonx_get

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/hello_watsonx")
def hello_watsonx():
    return watsonx_get("Hello WatsonX")