from flask import Flask, render_template, request, redirect, url_for, session
import os


app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')    

app.run()