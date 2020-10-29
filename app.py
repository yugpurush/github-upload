import os
from flask import Flask
import config

app = Flask(__name__)


from config import DevelopmentConfig
app.config.from_object(DevelopmentConfig())
#app.config.from_object(os.environ['APP_SETTINGS'])  

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()