from flask import Blueprint, redirect, url_for, render_template, session

bp_index = Blueprint('index', __name__, url_prefix='/')


@bp_index.route('/', methods=['GET'])
def index():
    # if 'user' in session:
        #return redirect(url_for('home.chatroom'))
    return redirect(url_for('auth.login'))





