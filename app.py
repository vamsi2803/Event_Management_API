from flask import Flask
from routes import api
from models import db
from config import Config
from flask_cors import CORS
from flasgger import Swagger

app = Flask(__name__)
app.register_blueprint(api) 

CORS(app)

app.config.from_object(Config) 

db.init_app(app)

with app.app_context():
    db.create_all()

Swagger=Swagger(app,template={
    "swagger": "2.0",
    "info": {
        "title": "Event Management API",
        "description": "API documentation for the Event Management system",
        "version": "1.0.0"
    },
    "host": "localhost:5000",
    "basePath": "/",
    "schemes": [
        "http",
        "https"
    ],
    "tags": [
        {
            "name": "Events",
            "description": "Operations related to events"
        }
    ]
})

if __name__ == '__main__':
    app.run(debug=True)
