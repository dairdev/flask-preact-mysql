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

from models import *

@app.route('/')
def index():
    if 'userId' in session:
        return redirect(url_for('home'))

    return render_template('login.html')


@app.route('/home')
def home():
    if 'userId' not in session:
        return redirect(url_for('login'))

    return render_template('home.html', usuario=session['username'])


@app.route('/documents')
def documents():
    if 'userId' not in session:
        return redirect(url_for('login'))

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


@app.route('/logout')
def logout():
    session.pop('userId', None)
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/upload', methods=['POST'])
def upload():
    isthisFile=request.files.get('file')
    print(isthisFile)
    print(isthisFile.filename)
    isthisFile.save("./UPLOADED/"+isthisFile.filename)
    doc = DocumentManager
    doc.saveDocument(isthisFile.filename, int(session['userId']))
    result = doc.listDocuments()
    return jsonify(files=result)


@app.route('/document/delete', methods=['POST'])
def deleteDocument():
    data = request.get_json(force=True)
    print('Data', data)
    if data is None:
        return jsonify(result=False)

    document = Document.query.filter_by(id=int(data.get('id'))).first()
    if document is None:
        return jsonify(result=False)


    doc = DocumentManager
    doc.deleteDocument(document)

    return jsonify(result=True)


@app.route('/documents/list', methods=['GET'])
def listDocuments():
    doc = DocumentManager
    result = doc.listDocuments()
    return jsonify(files=result)
    
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
