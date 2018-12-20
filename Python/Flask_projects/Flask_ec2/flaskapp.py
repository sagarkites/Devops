from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

# Decorator
@app.route('/movie')
def hello_world():
# Render Html Pages  
  return render_template('movie.html')

@app.route('/sagar')
def iam():
    return 'Think Globally Act Locally'

@app.route('/', methods=['GET', 'POST'])
# Using Html Methods
def login():
    error = None
    if request.method == 'POST':
# authentication to Login Credentials
        if request.form['username'] != 'sagar' or request.form['password'] != 'sagar215':
            error = 'Invalid Credentials'
        else:
# Redirecting to specific Endpoint          
            return redirect(url_for('hello_world'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
  app.run()

