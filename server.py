from flask import Flask, render_template, request
import requests

app = Flask(__name__, static_url_path='', 
              static_folder='static', 
              template_folder='templates'
           )


@app.route('/')
def home():
    table = [['one','two','three'],['four','five','six'],['seven','eight','nine']]
    return render_template('index.html', item = table )


if __name__ == "__main__":
    app.run( port = 3001 )