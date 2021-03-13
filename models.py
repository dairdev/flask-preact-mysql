from app import db

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


