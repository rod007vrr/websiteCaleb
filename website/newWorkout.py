from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort

from website.auth import login_required
from website.db import get_db
from website.WktAnalysis.Classes.person import Person

bp = Blueprint('newWorkout', __name__)


@bp.route('/home/newWorkout', methods=('GET', 'POST'))
@login_required
def newWorkout():
    db = get_db()
    if request.method == 'POST':
        title = request.form['workoutTitle']
        workout = request.form['workoutBody']
        print(workout)
        error = None
        if not workout or not title:
            error = 'Body is required'
            
        if error is not None:
            flash(error)
        else:
            temp = Person()
            workoutCopy = [n.removesuffix("\r") for n in workout.split("\n")]
            temp.updateStats(workoutCopy)
            numbers = str(temp.bodyTree.printTree([]))
            
            db = get_db()
            db.execute(
                'INSERT INTO userWorkout (title, descript, author_id, bodyData)'
                ' VALUES (?, ?, ?, ?)',
                (title, workout, g.user['id'], numbers)
            )
            db.commit()
            
            if error is None:
                if session["isCoach"] == 1:
                    return redirect(url_for("coachHome.coachHome"))
                return redirect(url_for("home.home"))
        
    return render_template("home/newWorkout.html")