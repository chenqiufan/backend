from apps import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(120),unique=True)
    phonenumber = db.Column(db.String(120),unique=False)
    password = db.Column(db.String(120),unique=True)

    def __repr__(self):
        return '<User : %s>' % self.username


db.create_all()
