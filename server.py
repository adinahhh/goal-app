from flask import Flask, render_template, request, flash, redirect, session

from jinja2 import StrictUndefined

from flask_debugtoolbar import DebugToolbarExtension

from model import User, Goals, connect_to_db, db

app = Flask(__name__)

#for flask sessions
app.secret_key = 'SECRETSECRETSECRET'

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """ Homepage with user login/sign-up form"""

    return render_template('homepage.html')


# register new user
@app.route('/registration', methods=['POST', 'GET'])
def register_user():
    """Show user registration form for app, OR create a new user for app"""

    if request.method == 'POST':
        email = request.form.get('email')
        confirm_existing_user = User.query.filter(User.email == email).all()
        if len(confirm_existing_user) == 0:
            dreamer = User(name=name, email=email, password=request.form.get('password'))
            db.session.add(dreamer)
            db.session.commit()
            flash('New dreamer account successfully created')
        else:
            flash('This email belongs to an existing user, please log in')

        # getting user name from dB
        # getting user_goals from dB
        user = User.query.filter_by(name=name)
        goals = Goals.query.filter_by(goal_info=goal_info)
        return redirect('profile_page.html', user=user, goals=goals)

    return render_template('registration.html')

# login new user
app.route('/login_form')
def show_login_form():
    """Displays login form for existing user"""

    return render_template('login_form.html')

@app.route('/login')
def login_existing_user():
    """logs in existing user from login_form"""

    email = request.form.get('email')
    password = request.form.get('password')

    verify_existing_user = User.query.filter(User.email == email, User.password == password).all()

    if len(verify_existing_user) > 0:
        session['user_id'] = verify_existing_user[0].user_id
        flash('You have been successfully logged in!')
 
        return render_template('profile_page.html')
    else:
        flash("Login information doesnt match an existing user. Please create a new account.")
        return redirect('/registration')

@app.route('/logout')
def logout_users():
    """Logs out any existing user from current session"""

    flash('You are logged out!')

    if session.get('user_id'):
        del session['user_id']
    return redirect('/')



if __name__ == "__main__":
    # uses the debugtoolbar extension
    app.debug = True
    # ensures templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host='0.0.0.0', port=5000)