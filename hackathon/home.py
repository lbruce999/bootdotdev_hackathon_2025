from flask import Blueprint, render_template


bp = Blueprint('home', __name__)


@bp.route('/')
def index():
    return render_template('home/index.html')
