from app import db
from datetime import date
from flask_sqlalchemy import SQLAlchemy

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


class DocumentManager:

    def saveDocument(fileName, userId):
        today = date.today()
        doc = Document(fileName, userId, today)
        db.session.add(doc)
        db.session.commit()

    def listDocuments():
        data = Document.query.all()
        cols = ['id', 'fileName']
        result = [{col: getattr(d, col) for col in cols} for d in data]
        return result

    def deleteDocument(document):
        db.session.delete(document)
        db.session.commit()
