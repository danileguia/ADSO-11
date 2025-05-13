from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "<h1>Primera aplicación web</h1>"

