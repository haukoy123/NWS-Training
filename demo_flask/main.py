from crypt import methods
from flask import Flask, redirect, url_for, Blueprint



app = Flask(__name__, template_folder='flaskr/templates', static_folder='flaskr/static')

from flaskr import create_app
from flaskr.test import test
from flaskr.login import login
from flaskr.login import bp


@app.route('/')
def hello():
    print('abc')
    return 'Hello, World!'




app.add_url_rule("/test", endpoint='test', view_func=test)  

# app.add_url_rule('/login', endpoint='login',view_func=login, methods=['POST', 'GET'])


app.register_blueprint(bp)


@app.route('/hello/<name>')
def hello_guest(name):
   return 'Hello %s ' % name

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
        return redirect(url_for('hello')) 
   else:
        return redirect(url_for('test'))


if __name__ == "__main__":
    app.debug = True
    app.run()
    

