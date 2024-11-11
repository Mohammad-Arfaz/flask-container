from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "flaska-app containerization"

@app.route('/home')
def hello():
    return 'flask-app'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3080)