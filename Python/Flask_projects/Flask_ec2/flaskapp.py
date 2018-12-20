from flask import Flask, render_template
app = Flask(__name__)
# Decorator
@app.route('/')
def hello_world():
# Setting Html file in script  
  return render_template('movie.html') 

if __name__ == '__main__':
  app.run()
