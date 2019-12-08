from flask_restplus import Namespace, fields


class TodoDTO:
    api = Namespace("todos", description="Todo related operations")
    todo = api.model(
        "Todo",
        {
            "todo_id": fields.String(description="task Identifier"),
            "task_description": fields.String(
                required=True, description="The task details"
            ),
            "created_at": fields.DateTime(description="The creation date of the task"),
            "last_edited_at": fields.DateTime(
                description="The last time the task was modified"
            ),
        },
    )
