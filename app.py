from flask import Flask, request, render_template
from backend import calls
import json


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/form', methods=['POST'])
def form():
    test = []
    domain = request.form['domain']
    blah = calls.malcoreDomainCheck(domain)
    
    return render_template('index.html', checked=check)


if __name__ == '__main__':
    app.run(debug=True)