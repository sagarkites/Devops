from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/devops')
def devops():
	return render_template('web.html')

if __name__ == '__main__':
   app.run(debug = True)	
