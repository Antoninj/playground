from flask_restplus import Api
from .todos_namespace import api as todos_namespace

api = Api(title="Anto's API", version="1.0", description="A simple REST API",)
api.add_namespace(todos_namespace)
