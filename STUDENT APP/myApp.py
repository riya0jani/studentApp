from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return {
        "status": "SUCCESS",
        "data":{
            "regno": 1847207,
            "name": "ALWIN",
            "email": "alwin.joseph@mca.christuniverse.in"
        }
    }


sdfs

if __name__ == "__main__":
    app.run(debug=True)