from flask import Flask, render_template

app = Flask(__name__) #this creates a usable instance of the flask class and saves it into the var app

@app.route("/") #this maps the url / to the python function index
def index():
    return render_template("index.html") #the python function uses the flask 'render template' to render the template 'index.html'

#so when the user types in the url/, the function index will run, and return the page index.html

#then the obligatory if statement:

if __name__ == "__main__":
    app.run(debug=True) #app.run runs the app on a local server


