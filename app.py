
from flask import Flask
from flask import render_template
from datetime import datetime
import re
app = Flask("flask")

@app.route("/")
def home():
    return render_template('home.tpl')

# New functions
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


"""
@app.route("/")
def home():
    return render_template("home.html")

# New functions
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)






#verk 1

@app.route('/')
def homepage():
#    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return #
    <h1>Hello heroku</h1>
    <p>It is currently {datetime}.</p>
    <img src="http://loremflickr.com/600/400" />
    ##.format(time=the_time)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/sida2")
def s2():
    return #
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    <img src="http://loremflickr.com/600/400" />
    #.format(time=the_time)

@app.route("/sida3")
def s3():
    return "sida 3"


@app.route("/hello_there")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

"""