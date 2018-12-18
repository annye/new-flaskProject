"""
Routes and views for the flask application.
"""
from flask import Flask, render_template, url_for,request
from flask_bootstrap import Bootstrap
from datetime import datetime



app = Flask(__name__)
Bootstrap(app)


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/Experiment')
def experiment():
    """Renders the contact page."""
    return render_template(
        'Experiments.html',
        title='Experiment',
        year=datetime.now().year,
  
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
      ) 

@app.route('/chat')
def chat():
    """Renders the Chat rooms template page."""
    return render_template(
        'chat.html',
        title='Chat Rooms',
        year=datetime.now().year,
    )






if __name__ == '__main__': 
	app.run(debug=True)