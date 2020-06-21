# Working directory should be microblog folder - flask run to be run from that folder
# Environment variables have set the FLASK_APP = microblog.py

from app import app, db
from app.models import User, Post

# Using flask shell (shell context) (instead of regular cmd line) pre-imports application instance, and other entities (e.g. database)
# This will start up an interactive Python shell, setup the correct application context and setup the local variables in the shell.


@app.shell_context_processor
def make_shell_context():
    # The reason the function returns a dictionary and not a list is that for each item you have to also provide a name (dict keys)
    # under which it will be referenced in the shell.
    return {"db": db, "User": User, "Post": Post}
