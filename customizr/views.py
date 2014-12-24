
import uuid
from flask import render_template
from customizr import app

@app.route('/')
def root():
    return render_template('home.html')
