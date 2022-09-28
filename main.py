from flask import Flask, render_template

# import the blueprints
from api.answers import api_answers


# initialize the flask app
app = Flask(__name__, static_url_path='')

# register the api blueprint
app.register_blueprint(api_answers)


# handle the index page
@app.route('/')
def index():

    # render the index.html file
    return render_template("index.html")


# handle the 404 error
@app.errorhandler(404)
def page_not_found(e):

    # render the 404.html template
    return render_template("404.html"), 404


# start the flask app port 5000
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
