from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/hello1")
def hello_world1():
    return "Hello, World1!"

@app.route("/hello2")
def hello_world2():
    return "Hello, World2!"

@app.route("/test_func")
def test():
    a= 5+6
    return("This is my first function in flask {}".format(a))

@app.route("/input_url")
def request_input():
    data= request.args.get('x')
    return "This is my input from the url {}".format(data)

## the url will need to be given in the following format
## https://blue-accountant-jfiiu.pwskills.app:5000/input_url?x=vishal

if __name__=="__main__":
    app.run(host="0.0.0.0")
