
from flask import Flask, redirect, url_for, request, render_template, Blueprint
# app = Flask(__name__)

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=('GET', 'POST'))
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('auth.success', name=user))
   else:
      return render_template('auth/login.html')


@bp.route('/success/<name>')
def success(name):
   return render_template('auth/success.html', name=name)