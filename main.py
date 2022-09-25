from flask import Flask, render_template, abort

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)