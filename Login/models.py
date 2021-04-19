from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin,LoginManager

# making a login manager object to hold user ID in the seesion
login = LoginManager()

# making a database instance object. 
db = SQLAlchemy()

# defining a new class for usermodel
# it stores email, username and password_hash
# this database extends userMixin
class UserModel(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), unique=True)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String())

# here i make functions that generates and checks a hash code for a 
# specific user-selected password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return UserModel.query.get(int(id))