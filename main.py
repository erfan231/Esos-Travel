from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        pass

@app.route("/couple", methods=["GET"])
def couple():
    if request.method == "GET":
        return render_template("couple.html")
    else:
        pass

@app.route("/family", methods=["GET"])
def family():
    if request.method == "GET":
        return render_template("family.html")
    else:
        pass

@app.route("/bali", methods=["GET"])
def bali():
    if request.method == "GET":
        return render_template("bali.html")
    else:
        pass

@app.route("/paris", methods=["GET"])
def paris():
    if request.method == "GET":
        return render_template("paris.html")
    else:
        pass

@app.route("/St.Lucia", methods=["GET"])
def dubai():
    if request.method == "GET":
            return render_template("St.Lucia.html")
    else:
        pass

@app.route("/turkey", methods=["GET"])
def turkey():
    if request.method == "GET":
        return render_template("turkey.html")
    else:
        pass


@app.errorhandler(404)
def not_found(error_404):
    return render_template("404.html")

#app.run(debug=True) #debug mode is on

 #The default hosting server is 127.0.0.1 and port is 5000. If your want to change it
#host="192.168.20.1", port=444(What ever port is available) 

#app.run(debug=True, host="192.168.79.1", port=5000)