from flask import (Blueprint, request, session, render_template, redirect, url_for, g, flash)

from dao.user import User
from forms.login import LoginForm
from utils import mylogger

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')


@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        logger = mylogger.get_logger()
        logger.info("Starting login process for user: " + form.username.data)
        if form.validate_on_submit():
            auth = request.form
            verify = User(user=auth['username'], password=auth['password'])
            isvalid = verify.verify_user()
            if isvalid:
                logger.info('User Verified')
                session['user'] = request.form['username']
                logger.info('redirecting to Home')
                return redirect(url_for('home.chatroom'))
            else:
                return redirect(url_for('index.index'))
        flash('User data required')
    if 'user' in session:
        session.clear()

    return render_template('login.html', title='Sign In', form=form)


@bp_auth.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('index.index'))


# @bp_auth.before_request
# def csrf_protect():
#     if request.method == "POST":
#         token = session.pop('_csrf_token', None)
#         if not token or token != request.form.get('_csrf_token'):
#             abort(403)

@bp_auth.before_request
def clean_session():
    session.clear()
