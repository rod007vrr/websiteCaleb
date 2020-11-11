from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from website.auth import login_required
from website.db import get_db

bp = Blueprint('home', __name__)

@bp.route('/home/home', methods=("GET", "POST"))
@login_required
def home():
    db = get_db()
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
    weeklySummary = "test string"
    if request.method == 'POST':
        body = request.form['journal']
        error = None
        if not body:
            error = 'Body is required'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO journalPosts (body, author_id)'
                ' VALUES (?, ?)',
                (body, g.user['id'])
            )
            db.commit()
    return render_template("home/home.html", 
    feedPosts=feedPosts, journalPosts=journalPosts, 
    exercises=exercises, weeklySummary=weeklySummary)
