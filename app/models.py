from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    token = db.Column(db.String(12), index=True, unique=True)
    iv_string = db.Column(db.String(16))
    encryption_key = db.Column(db.String(12))

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Vault(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_four = db.Column(db.Integer)
    card_token = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    uuid = db.Column(db.String(128), index=True, unique=True)
