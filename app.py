from flask import Flask
from flask import render_template
from flask import  request, jsonify
from packages import packages_list
from destinations import  destination_list
from tourist_places import  tour_list

app = Flask(__name__)

@app.route("/")
def homepage():
    packages = packages_list()
    destinations = destination_list()
    return render_template('index.html', packages=packages, destinations=destinations)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/services")
def services():
    tours = tour_list()
    return render_template('services.html', tours=tours)

@app.route("/packages")
def packages():
    packages = packages_list()
    destinations = destination_list()
    return render_template('packages.html', packages=packages, destinations=destinations)

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/booking")
def booking():
    image = request.args.get('image')
    return render_template('booking.html', image=image)

@app.route("/subscribe", methods=["GET", "POST"])
def subscribe():
    if request.method == "POST":
        email = request.form.get("Email")
        with open("subscriber_list.txt", 'a') as fh:
            fh.write(email + "\n")
    return jsonify({"message": "Subscribe API called successfully!"})

@app.route("/test")
def test():
    return render_template('test.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
