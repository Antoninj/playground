from flask_restplus import Resource

from app.main.controller.todo_dao import TodoDAO
from app.main.model.todo_dto import TodoDTO

api = TodoDTO.api

todo = TodoDTO.todo

DAO = TodoDAO(api)
DAO.create({"task": "Build an API"})
DAO.create({"task": "?????"})
DAO.create({"task": "profit!"})


@api.route("/")
class TodoList(Resource):
    """Shows a list of all todos, and lets you POST to add new tasks"""

    @api.doc("list_todos")
    @api.marshal_list_with(todo)
    def get(self):
        """List all tasks"""
        return DAO.todos

    @api.doc("create_todo")
    @api.expect(todo)
    @api.marshal_with(todo, code=201)
    def post(self):
        """Create a new task"""
        return DAO.create(api.payload), 201


@api.route("/<int:id>")
@api.response(404, "Todo not found")
@api.param("id", "The task identifier")
class Todo(Resource):
    """Show a single todo item and lets you delete them"""

    @api.doc("get_todo")
    @api.marshal_with(todo)
    def get(self, id):
        """Fetch a given resource"""
        return DAO.get(id)

    @api.doc("delete_todo")
    @api.response(204, "Todo deleted")
    def delete(self, id):
        """Delete a task given its identifier"""
        DAO.delete(id)
        return "", 204

    @api.expect(todo)
    @api.marshal_with(todo)
    def put(self, id):
        """Update a task given its identifier"""
        return DAO.update(id, api.payload)
