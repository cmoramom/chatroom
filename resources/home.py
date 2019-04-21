from flask import (Blueprint, render_template, session, redirect, url_for, g)

bp_home = Blueprint('home', __name__, url_prefix='/')


@bp_home.route('/home', methods=('GET', 'POST'))
def chatroom():
    if 'user' in session:
        user = session['user']
        return render_template('home.html', user=user)
    return redirect(url_for('auth.login'))

