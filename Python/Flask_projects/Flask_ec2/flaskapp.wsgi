import sys
sys.path.insert(0, '/var/www/html/flaskapp')
# WSGI is a simple calling convention for web servers to forward requests to web applications or frameworks  
from flaskapp import app as application
