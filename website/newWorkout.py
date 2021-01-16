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
            db = get_db()
            db.execute(
                'INSERT INTO userWorkout (title, descript, author_id)'
                ' VALUES (?, ?, ?)',
                (title, workout, g.user['id'])
            )
            db.commit()
            
            
            
            #autogen a 0 for everyone when first making
            
            temp = Person()
            workout = [n.removesuffix("\r") for n in workout.split("\n")]
            temp.updateStats(workout)
            print(temp.bodyTree.printTree([]))
            
            #work magic here
            #calc body changes and move to db
            #move workout as thing or whatever
            
            if error is None:
                if session["isCoach"] == 1:
                    return redirect(url_for("coachHome.coachHome"))
                return redirect(url_for("home.home"))
        
    return render_template("home/newWorkout.html")