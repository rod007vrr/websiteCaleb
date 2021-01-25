from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort

from website.auth import login_required
from website.db import get_db
import numpy


bp = Blueprint('coachHome', __name__)


@bp.route('/home/coachHome', methods=('GET', 'POST'))
@login_required
def coachHome():
    db = get_db()
    if session["isCoach"] == 0:
        return redirect(url_for("home.home"))
    userList = db.execute(
        "SELECT id, username, isCoach"
        " FROM user"
        " ORDER BY id DESC"
    )
    feedPosts = db.execute(
        "SELECT title, body, created"
        " FROM feedPosts"
        " ORDER BY created DESC"
    ).fetchall()
    journalPosts = db.execute(
        'SELECT p.id, body, created, author_id, username'
        ' FROM journalPosts p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    exercises = db.execute(
        "SELECT title, descript"
        " From exercises"
        " ORDER BY title"
    ).fetchall()
    workouts = db.execute(
        "SELECT id, title, descript, author_id, bodyData"
        " From userWorkout"
        " ORDER BY created"
    ).fetchall()
    if request.method == 'POST':
        title = request.form['postTitle']
        body = request.form['postBody']
        error = None

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO feedPosts (title, body)'
                ' VALUES (?, ?)',
                (title, body)
            )
            db.commit()
            return redirect(url_for("coachHome.coachHome"))
    return render_template('home/coachHome.html', feedPosts=feedPosts, journalPosts=journalPosts, exercises=exercises, userList=list(userList), workouts=workouts)
