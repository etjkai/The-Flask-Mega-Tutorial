from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Thomas"}
    posts = [
        {"author": {"username": "John"}, "body": "Beautiful day in Portland!"},
        {"author": {"username": "Susan"}, "body": "The Avengers movie was so cool!"},
    ]

    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    # Only True when POST, and all validators pass
    if form.validate_on_submit():
        # Flashed messages will be rendered in the template (base.html), in get_flashed_messages()
        flash(
            f"Login requested for user {form.username.data}, remember_me={form.remember_me.data}"
        )
        # Automatic navigation to a different page in argument
        return redirect(url_for("index"))

    return render_template("login.html", form=form, title="Sign In")

