from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.exceptions import abort

from website.auth import login_required
from website.db import get_db
from website.WktAnalysis.Classes.person import Person

bp = Blueprint('newExercise', __name__)


@bp.route('/home/newExercise', methods=('GET', 'POST'))
@login_required
def newExercise():
    db = get_db()
    exercises = db.execute(
        "SELECT title, descript"
        " FROM exercises"
        " ORDER BY title"
    )
    if request.method == 'POST':
        name = request.form['exerName']
        description = request.form['exerDescript']
        
        error = None
        if not name or not description:
            error = 'Body is required'
        if error is not None:
            flash(error)
            
        else:
            
            descCopy = [n.removesuffix("\r") for n in description.split("\n")]
            
            db = get_db()
            db.execute(
                'INSERT INTO exercises (title, descript)'
                ' VALUES (?, ?)',
                (name, description)
            )
            db.commit()
            
            if error is None:
                return redirect(url_for("newExercise.newExercise"))
        
    return render_template("home/newExercise.html", exercises=exercises)