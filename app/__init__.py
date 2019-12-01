from flask_restplus import Api
from flask import Blueprint
from app.main.controller.todos_controller import api as todos_namespace

blueprint = Blueprint("api", __name__)

api = Api(
    blueprint, title="Anto's API", version="1.0", description="A simple REST API",
)
api.add_namespace(todos_namespace, path="/todos")
