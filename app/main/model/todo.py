from app.main import db


class Todo(db.Model):
    """ Todo Model for storing todos related details """

    __tablename__ = "todo"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    todo_id = db.Column(db.String(100), unique=True)
    task__description = db.Column(db.String(255), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    last_edited_at = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return "<Task '{}'>".format(self.task_description)
