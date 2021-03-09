from flask import current_app, flash, Flask, Markup, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import dbusername, dbpassword, dbhost, dbname 

app = Flask(__name__)
app.debug = False
app.testing = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{dbusername}:{dbpassword}@{dbhost}:3306/{dbname}'.format(
    dbusername=dbusername,
    dbpassword=dbpassword,
    dbname=dbname,
    dbhost=dbhost
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'User'
    
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    login = db.Column(db.String(30), unique=True, nullable=False)
    pwd = db.Column(db.String(30), unique=True, nullable=False)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html', usuario='test')


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return index()
    else:
        user = User.query.filter_by(login=request.form['user']).first()
        if user is None:
            error = 'Usuario/Password errado'
            return render_template('login.html', error=error)
        else:
           if user.pwd != request.form['password']:
               error = 'Usuario/Password errado'
               return render_template('login.html', error=error + '/' + user.login + '|' + user.pwd + ' ' + request.form['password'])

        return render_template('home.html', usuario=request.form['user'])


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
