from flask import Flask # import flask obj from FLask
from .db_model import db

def create_app():
    '''
       create an configure an instance of the flask application;
       wrap our app in this fcn so when we call it inside the init.py,
       it'll get initialized when we run our Twitoff app 
    '''
    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///C:\\Users\\bruno\\Desktop\\DSPT6-Twitoff\\twitoff\\twitoff.sqlite"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/theda/Desktop/twitoff-pt6/twitoff/twitoff.sqlite" # creates db ..repo/pkg/name our db to make
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # remove this low-use features tracks db modifications & allows some actions); remove to save memory
    db.init_app(app) # included when he got Assertion Err: The sqlalchmy extn was not regstrd 2 curr app..CAll init_app() 1st; 1:42:35

    @app.route('/')
    def root():
        # return 'Welcome to Twitoff!' #we'll render a tempL8, a jinja fnclty- instd of rtn str, rtn othr info
        return render_template('base.html', title='Home', users=User.query.all()) # render an HTML template
    return app
'''
    app = Flask(__name__) #app obj; Cre8 app inst here and rtn it (make it accessible) to init.py; pass __name__  is name of file passed to Flask class

    @app.route('/') # decorator (does what? Bruno ~agreed to Devvin's "creates a path") for this app; '/' is homepage
    def hello_world():
        return 'Welcome to Twitoff!' #we'll render a tempL8, a jinja fnclty- instd of rtn str, rtn othr info
'''
    