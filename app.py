from datetime import datetime
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a080735da135a614f98ad61116dd233d'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/rating')
def rating():
    return render_template('rating.html')


@app.route('/problems')
def problems():
    return render_template('problems.html')


@app.route('/education')
def education():
    return render_template('education.html')


@app.route('/olympiad')
def olympiad():
    return render_template('olympiad.html')


@app.route('/help')
def help():
    return render_template('help.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'bitara@posta.ge' and form.password.data == '12345678':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash(f'Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
