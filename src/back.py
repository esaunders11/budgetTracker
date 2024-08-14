from flask import Flask , request, render_template, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATOINS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)


db = SQLAlchemy(app)

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String(100))
    psw = db.Column(db.String(100))
    purchases = db.relationship('purchases', backref='users')

    def __init__(self, uname, psw):
        self.uname = uname
        self.psw = psw

class purchases(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    week = db.Column(db.Integer)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    expenses = db.relationship('expenses', backref="purchases")

    def __init__(self, week, expenses):
        self.week = week
        self.expenses = expenses

class expenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(100))
    price = db.Column(db.Integer)
    purchases_id = db.Column(db.Integer, db.ForeignKey('purchases.id'))

    def __init__(self, item, price):
        self.item = item
        self.price = price



@app.route('/')
def page():
    return render_template('index.html')


@app.route("/")
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["uname"]
        session["user"] = user

        found_user = users.query.filter_by(name=user).first()
        if found_user:
            session["data"] = found_user
            usr = users(user, "")
            db.session.add(usr)
            db.session.commit()

@app.route("/", methods=["POST", "GET"])
def user():
    uname = None
    psw = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            uname = request.form["uname"]
            psw = request.form["psw"]
            session["uname"] = uname
            session["psw"] = psw
            flash("Username and Password saved")
        else:
            if "uname" in session:    
                uname = session["uname"]
                psw = session["psw"]
    else:
        flash("already logged in")




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)