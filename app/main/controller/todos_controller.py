from flask import request
from flask_restplus import Resource, cors

from app.main.model.todo_dto import TodoDTO
from app.main.service.todo_service import (
    get_all_todos,
    save_new_todo,
    get_todo,
    delete_todo,
)
from app.main.util.auth_decorator import token_required

api = TodoDTO.api

_todo = TodoDTO.todo


@cors.crossdomain(origin="*")
@api.route("/")
class TodoList(Resource):
    """Shows a list of all todos, and lets you POST to add new tasks"""

    @api.doc("list_todos")
    @api.marshal_list_with(_todo)
    def get(self):
        """List all tasks"""
        return get_all_todos()

    @api.doc("create_todo")
    @api.expect(_todo, validate=True)
    @token_required
    @api.marshal_with(_todo, code=201)
    @api.response(201, "Todo successfully created.")
    def post(self):
        """Create a new task"""
        data = request.json
        return save_new_todo(data=data), 201


@cors.crossdomain(origin="*")
@api.route("/<todo_id>")
@api.response(404, "Todo not found")
@api.param("todo_id", "The task identifier")
class Todo(Resource):
    """Show a single todo item and lets you delete them"""

    @api.doc("get_todo")
    @api.marshal_with(_todo)
    def get(self, todo_id):
        """Fetch a given resource"""
        todo = get_todo(todo_id)
        if not todo:
            api.abort(404, "Todo {} doesn't exist".format(todo_id))
        else:
            return todo

    @api.doc("delete_todo")
    @api.response(204, "Todo deleted")
    def delete(self, todo_id):
        """Delete a task given its identifier"""
        todo = get_todo(todo_id)
        if not todo:
            api.abort(404, "Todo {} doesn't exist".format(todo_id))
        else:
            delete_todo(todo_id)
            response_object = {
                "status": "success",
                "message": "Todo {} successfully deleted".format(todo_id),
            }
            return response_object, 204

    @api.doc("update_todo")
    @api.expect(_todo, validate=True)
    @api.marshal_with(_todo)
    def put(self, todo_id):
        """Update a task given its identifier"""
        return DAO.update(todo_id, api.payload)
