## Install the apache webserver and mod_wsgi:
```
sudo apt-get update
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi
```
## Install Flask using the pip tool
```
sudo apt-get install python-pip
sudo pip install flask
```
## Create a directory for our Flask app
```
mkdir ~/flaskapp
sudo ln -sT ~/flaskapp /var/www/html/flaskapp
```
## To verify our operation is working, create a simple index.html file
```
cd ~/flaskapp
echo "Hello World" > index.html
```
## You should now see "Hello World" displayed if you navigate to (your instance public DNS)/flaskapp in your browser
Running a simple Flask app(flaskapp.py)
```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello from Flask!'

if __name__ == '__main__':
  app.run()
```
## Create a .wsgi file to load the app(flaskapp.wsgi)
```
import sys
sys.path.insert(0, '/var/www/html/flaskapp')

from flaskapp import app as application
```
## Enable mod_wsgi.
## In the apache configuration file located at /etc/apache2/sites-enabled/000-default.conf, add the following block just after the DocumentRoot /var/www/html line
```
WSGIDaemonProcess flaskapp threads=5
WSGIScriptAlias / /var/www/html/flaskapp/flaskapp.wsgi

<Directory flaskapp>
    WSGIProcessGroup flaskapp
    WSGIApplicationGroup %{GLOBAL}
    Order deny,allow
    Allow from all
</Directory>
```
## Restart the webserver
```
sudo apachectl restart
```
## If you navigate your browser to your EC2 instance's public DNS again, you should see the text returned by the hello_world function of our app, "Hello from Flask!"
