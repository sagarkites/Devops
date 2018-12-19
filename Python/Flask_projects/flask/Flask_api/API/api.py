from flask import Flask, render_template, flash, request, jsonify
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import wtforms_json 

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
wtforms_json.init()

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    password = TextField('Password:', validators=[validators.required()])
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    form.from_json(request.json)
    print form.data
    
    if form.validate():
       return jsonify(id = '1',
                      username = 'sagar',
                      gender = 'Male') 

    if request.method == 'POST':
        name=request.form['name']
        password=request.form['password']
        print name
        print password
        if form.validate():
            # Save the comment here.
            flash('Hello ' + name)

        else:
            flash('All the form fields are required. ')
 
    return render_template('register.html', form=form)
 
if __name__ == "__main__":
    app.run()        

  