from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# @app.route("/viewer")
# def viewer():
#     return render_template("viewer.html")

@app.route("/create_session", methods=['POST'])
def create_session():
    return render_template("viewer.html")

@app.route("/join_session", methods=['POST'])
def join_session():
    return "Session Joined"

if __name__ == "__main__":
    app.run(debug=True)