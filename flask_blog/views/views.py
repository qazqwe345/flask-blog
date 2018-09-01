from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app
from functools import wraps


def login_required(view):
    @wraps(view)
    def inner(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return view(*args, **kwargs)
    return inner

@app.errorhandler(404)
def non_existant_route(error):
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('Wrong Username')
        elif request.form['password'] != app.config['USERNAME']:
            flash('Wrong Password')
        else:
            session['logged_in'] = True
            flash('Login Succeeded')
            return redirect(url_for('show_entries'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    flash('Logout Succeeded')
    session.pop('logged_in', None)
    return redirect(url_for('show_entries'))


