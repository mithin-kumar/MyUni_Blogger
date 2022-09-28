from distutils.log import debug
from datetime import datetime
from flask_sqlalchemy import  SQLAlchemy
from flask import Flask,render_template,url_for,flash,redirect
from form import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']='bb06318b3b0392c10b30a24f78221aa9'

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'

db =SQLAlchemy(app)

class User(db.Model):
    id =db.Column(db.Integer ,primary_key=True)
    username= db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image=db.Column(db.String(20),nullable=False,default='default.jpg')
    password = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{{ self.username }}' ,'{{ self.email }}','{{ self.image }}')"

class Post(db.Model):
    id =db.Column(db.Integer ,primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False , default=datetime.utcnow)
    password = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f"User('{{ self.title }}' ,'{{ self.date_posted }}')"

posts=[
    {
        'author': 'mithin',
        'title': 'my blog',
        'content': 'Going Zero Waste is an eco-friendly blog started by Kathryn Kellogg, an advocate for a plastic-free and sustainable lifestyle. She blogs about zero waste, and her site is a perfect place to start if you want to join this movement. The site also features a book called 101 Ways to Go Zero Waste. 31. My Plastic-Free Life',
        'date_posted': 'April 20,2018'
    },
    {
        'author': 'hari',
        'title': 'my viewpoints',
        'content': 'Here are some personal bloggers that definitely fit the “niche” they have chosen to blog in. 7. Hyperbole and a Half Allie Brosh writes with humor and a lot of original cartoons. Lighthearted and fun. 8. Woogs World Mrs. Woog is a 40 something mom with bucketfuls of wit. Her blog will keep you smiling for sure. 9. The Book Smugglers',
        'date_posted': 'April 19,2018'
    }
]


@app.route("/")
def hello():
    return "<h1>hello </h1>"


@app.route("/about")
def about():
    return render_template('about.html',title='Abouttitle')


@app.route("/home")
def home():
    return render_template('index.html',posts=posts,title='Homepage')

@app.route("/register",methods=['GET','POST'])
def register():
    form= RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account created for {  form.username.data  } !','success')
        return redirect(url_for('home'))
    return render_template('register.html',title='register',form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        if form.email.data=='mithinkumar@gmail.com' and form.password.data=='mithin':
            flash('You Have LoggedIn Successfullly !')
            return redirect(url_for('home'))
        else:
            flash('Login unsuceessfull ! Invalid  email or Password','danger')
    return render_template('login.html',title='Login',form=form)
if __name__ == '__main__':
    app.run(debug=True)
