from flask import Flask
import os
from decouple import config

app = Flask(__name__)
appSetting = config('CONFIGURATION_SETUP')

print(appSetting)   #prints: config.DevelopmentConfig


app.config.from_object(appSetting)  

app.config['SECRET_KEY'] = config('SECRET_KEY')

print (app.config)

#print(f"Development: {app.config['DEVELOPMENT']}")
#print(f"Debug: {app.config['DEBUG']}")
print(f"Secret key: {app.config['SECRET_KEY']}")

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()