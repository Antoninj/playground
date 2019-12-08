import datetime
import uuid

from app.main import db
from app.main.model.todo import Todo


def save_new_todo(data):
    creation_date = datetime.datetime.utcnow()
    new_todo = Todo(
        todo_id=str(uuid.uuid4()),
        task_description=data["task_description"],
        created_at=creation_date,
        last_edited_at=creation_date,
    )
    save_changes(new_todo)
    return new_todo


def get_all_todos():
    return Todo.query.all()


def get_todo(todo_id):
    return Todo.query.filter_by(todo_id=todo_id).first()


def delete_todo(todo_id):
    todo = Todo.query.filter_by(todo_id=todo_id)
    todo.delete(synchronize_session=False)
    db.session.commit()


def save_changes(data):
    db.session.add(data)
    db.session.commit()
