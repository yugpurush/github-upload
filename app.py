from flask import Flask
from config import Config
import os

app = Flask(__name__)
appSetting = os.environ['CONFIGURATION_SETUP']
print(appSetting)   #prints None

app.config.from_object(appSetting)  

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

#export APP_SETTINGS="config.DevelopmentConfig"
if __name__ == '__main__':
    app.run()