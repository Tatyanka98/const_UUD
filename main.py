from flask import Flask, render_template, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin

app = Flask(__name__)
app.secret_key = 'UUD_epta'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)

app.app_context().push()

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(32), nullable = False, unique=True)
    password = db.Column(db.String(64), nullable=False)
    first_name = db.Column(db.String(32),nullable=False)
    last_name = db.Column(db.String(32), nullable=False, default=False)
    teacher = db.Column(db.Boolean(), nullable=False, default=False)
    admin = db.Column(db.Boolean(), nullable=False, default=False)

@manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

@app.route('/',methods=['GET','POST'])
@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/reg', methods=['GET','POST'])
def reg():
    flash('Пароли не совпадают')
    return render_template('reg.html')

if __name__ =='__main__':
    app.run(debug=True)