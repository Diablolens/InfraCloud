#FLASK APP SCRIPT
#FILL IN THE MISSING PARTS AND TEST IF THE FLASK SCRIPT RUNS 

from flask import Flask
from flask import request
from flask import render_template

import datetime

microweb_app = Flask(__name__)

@microweb_app.route("/")
def main():
    return render_template("index.html" , date_now = datetime.datetime.now())

if __name__ == "__main__":
    microweb_app.run(host="0.0.0.0", port=5050)
