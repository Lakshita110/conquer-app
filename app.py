from flask import Flask
import google.generativeai as palm 
import cgi 
from flask import render_template 
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')
    key = "AIzaSyAnF2Z_rCk2WxtUhkEOhKsi0XFAtBcanuk"
    palm.configure(api_key=key)
    model_id = 'models/text-bison-001'
    form = cgi.FieldStorage()  
    prompt = "What's the weather?"
    completion = palm.generate_text(
        model = model_id,
        prompt = prompt,
        temperature = 0.99
    )
    return f"<p>{completion.candidates[0]['output']}</p>"

    print("Content-Type: text/html")
    print()

    # Generate an HTML response
    print("<html>")
    print("<head><title>Python Script Response</title></head>")
    print("<body>")
    print("<h1>Python Script Response</h1>")
    print()
    print("</body>")
    print("</html>")
    return "<p>Hello, World!</p>"

@app.route('/process_form', methods=['POST'])
def process_form():
    task = request.form.get('name')
    time = request.form.get('email')

    # Process the form data (you can perform any action here)

    return f"Form submitted!"

