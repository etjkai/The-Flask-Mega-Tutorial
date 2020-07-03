from flask import render_template
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    # Default value of second return value is 200 (Successful)
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    # Resets session to a clean slate // opposite of db.session.commit()
    db.session.rollback()
    return render_template('500.html'), 500