from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz
import getpass

app = Flask(__name__)

@app.route("/htop")
def htop():
    full_name = "Vishal Malge"
    username = getpass.getuser()
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")
    top_output = subprocess.getoutput("top -b -n 1 | head -20")

    html = f"""
    <html>
    <head><title>/htop</title></head>
    <body>
        <h2>Name: {full_name}</h2>
        <h3>Username: {username}</h3>
        <h3>Server Time (IST): {server_time}</h3>
        <pre>{top_output}</pre>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
