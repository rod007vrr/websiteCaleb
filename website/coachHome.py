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
        '''
        name = request.form['exerName']
        descript = request.form['exerDescript']
        '''
        error = None


        values = numpy.zeros((2,2), dtype=int)
        formChoice = None
        
        if title:
            values[0,0] = 1
        if body:
            values[0,1] = 1
        '''
        if name:
            values[1,0] = 1
        if descript:
            values[1,1] = 1
        '''
        
        for n in values[0]:
            if n != 0:
                formChoice = 0
            else:
                formChoice = 1
        for n in values[formChoice]:
            if n == 0:
                error = 'Missing data in form'
        if error is not None:
            flash(error)
        else:
            db = get_db()
            if formChoice == 0:
                db.execute(
                    'INSERT INTO feedPosts (title, body)'
                    ' VALUES (?, ?)',
                    (title, body)
                )
            '''
            if formChoice == 1:
                db.execute(
                    'INSERT INTO exercises (title, descript)'
                    ' VALUES (?, ?)',
                    (name, descript)
                )
            '''
            db.commit()
            return redirect(url_for("coachHome.coachHome"))
    return render_template('home/coachHome.html', feedPosts=feedPosts, journalPosts=journalPosts, exercises=exercises, userList=list(userList), workouts=workouts)
