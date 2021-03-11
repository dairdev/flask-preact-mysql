from flask import current_app, flash, Flask, Markup, redirect, render_template, request, session, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import dbusername, dbpassword, dbhost, dbname
from datetime import date

app = Flask(__name__)
app.debug = False
app.testing = False

app.config['SECRET_KEY'] = 'M]39RCGWdXWn@MLH"D3uET;F(4X[Xc'

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


class Document(db.Model):
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    fileName = db.Column(db.String(30), unique=True, nullable=False)
    uploadedBy = db.Column(db.Integer, nullable=False)
    uploadedOn = db.Column(db.DateTime, nullable=False)

    def __init__(self, fileName, uploadedBy, uploadedOn):
        self.fileName=fileName
        self.uploadedBy=uploadedBy
        self.uploadedOn=uploadedOn


def saveDocument(fileName):
    today = date.today()
    doc = Document(fileName, session['username'], today)
    db.session.add(doc)
    db.session.commit()


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('home.html', usuario=session['username'])


@app.route('/documents')
def documents():
    return render_template('documents.html', usuario=session['username'])


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

        session['userId'] = user.id
        session['username'] = request.form['user']
        return redirect(url_for('home'))


@app.route('/upload', methods=['POST'])
def upload():
    isthisFile=request.files.get('file')
    print(isthisFile)
    print(isthisFile.filename)
    isthisFile.save("./UPLOADED/"+isthisFile.filename)
    saveDocument(isthisFile.filename)
    return jsonify(fileUploaded=isthisFile.filename, files=Document.query.all())


@app.route('/files/list', methods=['GET'])
def listFilse():
    return jsonify(files=Document.query.all())
    
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
