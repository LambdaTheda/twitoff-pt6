'''Entry point into the Twitoff flask application'''

from .app import create_app

APP = create_app()  # when we set our evn var (FLASK_APP=twitoff:APP) this is waht's getting run (mod 2 vid 6:49), cre8s the app
# CAPS indic8 a global var; 
# L8r u3s3m1 vid 25:13 he says his assumption that it's
# GLOBAL was wrong so sets it 