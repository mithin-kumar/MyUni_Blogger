from distutils.log import debug
from flask import Flask,render_template,url_for,flash,redirect
from form import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY']='bb06318b3b0392c10b30a24f78221aa9'

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

@app.route("/login")
def login():
    form= LoginForm()
    return render_template('login.html',title='Login',form=form)
if __name__ == '__main__':
    app.run(debug=True)
