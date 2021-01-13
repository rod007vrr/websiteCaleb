from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort

from website.auth import login_required
from website.db import get_db


bp = Blueprint('newWorkout', __name__)


@bp.route('/home/newWorkout', methods=('GET', 'POST'))
@login_required
def newWorkout():
    db = get_db()
    
    
    if request.method == 'POST':
        title = request.form['workoutTitle']
        body = request.form['workoutBody']
        error = None
        if not body or not title:
            error = 'Body is required'
            
        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO userWorkout (title, descript, author_id)'
                ' VALUES (?, ?, ?)',
                (title, body, g.user['id'])
            )
            db.commit()
    return render_template("home/newWorkout.html")