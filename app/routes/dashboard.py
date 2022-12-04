from flask import Blueprint, render_template

bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route("/")
def dash():
    return render_template('dashboard.html')

@bp.route("/edi/<id>")
def edit(id):
    return render_template("edit-post.html")
