import os
import sys
import site

#
#This is an example config using a virtualenv called "python"
#This file goes in the root app directory (same folder as app.py)

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/var/www/flansible/flansible-env/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/var/www/flansible/flansible/Flansible')

# Activate your virtual env
activate_env=os.path.expanduser("/var/www/flansible/flansible-env/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

from flansible import app as application
