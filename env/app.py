import re
from flask import Flask
from datetime import datetime
app = Flask("flask")

@app.route('/')
def homepage():
#    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    <img src="http://loremflickr.com/600/400" />
    """#.format(time=the_time)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/sida2")
def s2():
    return """"
    <h1>Hello heroku</h1>
    <p>It is currently {time}.</p>
    <img src="http://loremflickr.com/600/400" />
    """#.format(time=the_time)"

@app.route("/sida3")
def s3():
    return "sida 3"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


    

"""@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"
    
    # BAD CODE! Avoid inline HTML for security reason, plus templates automatically escape HTML content.
    content = "<strong>Hello there, " + name + "!</strong> It's " + formatted_now
    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content
"""


"""
#TIL KENNARA!!!
#       |
#       |
#       V
#Til þess að finna Verkefni 1 þarf að fara á https://hrolfurgylfa.herokuapp.com/Verkefni_1 og til þess að finna verkefni tvö þarf að fara á https://hrolfurgylfa.herokuapp.com/Verkefni_2

from sys import argv
import bottle
from bottle import *


#Verkefni 1----------Verkefni 1----------Verkefni 1----------Verkefni 1----------Verkefni 1
@route("/Verkefni_1")
def Verkefni_1():
    return 
    <h2>Verkefni 1</h2>
    <a href="/um">Um mig</a>
    <a href="/aefisaga">Aefisaga min</a>
    <a href="/myndir">Myndir af mer</a>
#Um
@route("/Verkefni_1/um")
def um():
    return "Herna eru upplysingar um mig"

#Æfisaga
@route("/Verkefni_1/aefisaga")
def aefisaga():
    return "Herna er aefisagan min"

#Myndir
@route("/Verkefni_1/myndir")
def myndir():
    return "Herna eru myndir af mer"

#Verkefni 2----------Verkefni 2----------Verkefni 2----------Verkefni 2----------Verkefni 2
@route("/Verkefni_2")
def Verkefni_2():
    return """ """
    <h1>Verkefni 2</h1>
    <a href="/Verkefni_2/lidur_A">Liður A</a> - 
    <a href="/Verkefni_2/lidur_B">Lidur B</a>
    """"""
#Liður A
@route("/Verkefni_2/lidur_A")
def lidur_a():
    return """"""
    <h1>Verkefni 2 - Liður A</h1>
    <a href="/Verkefni_2/sida/1">Síða 1</a>
    <a href="/Verkefni_2/sida/2">Síða 2</a>
    <a href="/Verkefni_2/sida/3">Síða 3</a>
    """"""
#Liður B
@route("/Verkefni_2/lidur_B")
def lidur_b():
    return """"""
    <h2>Verkefni 2 - Liður A</h2>
    <h3>Veldu uppáhalds staf</h3>
    <img src="/Myndir/A.jpg">
    <img src="Myndir/B.jpg">
    <img src="Myndir/C.jpg">
    <img src="Myndir/D.jpg">
    """"""
#Liður A
@route("/Verkefni_2/sida/<id:int>")
def page(id):
    if id == 1:
        return "Þetta er síða 1<br><a href='/Verkefni_2/lidur_A'>Til baka</a>"

    elif id == 2:
        return "Þetta er síða 2<br><a href='/Verkefni_2/lidur_A'>Til baka</a>"

    elif id == 3:
        return "Þetta er síða 3<br><a href='/Verkefni_2/lidur_A'>Til baka</a>"

    else:
        return '<h2 style="color:red;text-align: center;">Þessi síða finnst ekki</h2>'

#Til þess að setja inn myndir
@route('/Myndir/<skra:path>')
def server_static(skra):
    return static_file(skra, root='Myndir')

#404 ERROR síða----------404 ERROR síða----------404 ERROR síða----------404 ERROR síða----------404 ERROR síða
@error (404)
def notFound(error):
    return '<h2 style="color:red;text-align: center;">Þessi síða finnst ekki</h2>'


#bottle.run(host="localhost", port=8080, reloader=True, debug=True)
bottle.run(host='0.0.0.0', port=argv[1])
"""