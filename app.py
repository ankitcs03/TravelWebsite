from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/packages")
def packages():
    return render_template('packages.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/booking")
def booking():
    return render_template('booking.html')

@app.route("/test")
def test():
    return render_template('test.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
