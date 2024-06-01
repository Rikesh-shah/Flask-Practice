from flask import Flask, flash, redirect, url_for, request, render_template

app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error= None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'invalid username or password. Please try again!'

        else:
            flash('you were successfully logged in')
            flash('Logout before logging again')
            return redirect(url_for('index'))
    return render_template('log_in.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)