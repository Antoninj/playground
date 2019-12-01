from flask_restplus import Namespace, fields


class TodoDTO:
    api = Namespace("todos", description="TODO operations")
    todo = api.model(
        "Todo",
        {
            "id": fields.Integer(
                readOnly=True, description="The task unique identifier"
            ),
            "task": fields.String(required=True, description="The task details"),
        },
    )
