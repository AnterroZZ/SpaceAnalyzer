from flask import Flask, render_template
import matplotlib.pyplot as plt
import os
import webbrowser

posts = [
    {
        'author': 'Andrzej Smolinski',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 11 2020'
    }
]

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return "<h1>About Page</h1>"


                
if __name__ == '__main__':
    if os.name is 'nt':
        os.system("set FLASK_APP=analyzer.py") 
        os.system("set FLASK_DEBUG=1")
    else:
        os.system("export FLASK_APP=analyzer.py") 
        os.system("export FLASK_DEBUG=1")
    webbrowser.open('http://localhost:5000', new=2)
    app.run(debug=True)
    