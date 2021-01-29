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
    workouts = db.execute(
        "SELECT id, title, descript, author_id, bodyData"
        " From userWorkout"
        " ORDER BY created DESC"
    ).fetchall()
    
    allData = []
    
    for n in range(5):
        allData.append([int(n) for n in workouts[n]["bodyData"][1:-1].split(",")])
    
    bodyParts = ["Body", "Upper", "Back", 
                 "Trapezius", "Rhomboids", "Latissimus", 
                 "Erector spinae", "Shoulders", "Anterior deltoid", 
                 "Lateral deltoid", "Posterior deltoid", "Chest", 
                 "Pectoralis major", "Upper pectoralis major", 
                 "Lower pectorals major", "Arms", "Upper arm", 
                 "Tricep", "Bicep", "Forearm", "Core", "Rectus abdominis", 
                 "Obliques", "Lower", "Thighs", "Quadriceps", "Hamstrings", 
                 "Gluteus", "Adductors", "Abductors", "Calves", "Outer calf", 
                 "Inner calf", "Frontal calf"]
    
        
    sumData = len(bodyParts)*[0]
    
    for n in range(len(bodyParts)):
        for x in range(5):
            sumData[n] += allData[x][n]
    
    dataToPrint = [bodyParts[n] + ": " + str(sumData[n]) for n in range(len(bodyParts))]
    print(dataToPrint)
    
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
            return redirect(url_for("home.home"))
    return render_template("home/home.html", 
    feedPosts=feedPosts, journalPosts=journalPosts, 
    exercises=exercises,  workouts=workouts, dataToPrint = dataToPrint)
