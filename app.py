from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/classes/')
def about():
    return render_template('classes.html')


@app.route('/weapons/')
def about():
    return render_template('weapons.html')


@app.route('/locations/')
def about():
    return render_template('locations.html')


if __name__ == '__main__':
    app.run()
