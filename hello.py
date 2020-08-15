from flask import Flask # import flask obj from FLask

app = Flask(__name__) #app obj; pass __name__  is name of file passed to Flask class

@app.route('/') # decorator (does what? Bruno ~agreed to Devvin's "creates a path") for this app ; '/' is homepage
def hello_world():
    return 'Hello, World!'

@app.route("/about")
def about():
    return "About Me..."