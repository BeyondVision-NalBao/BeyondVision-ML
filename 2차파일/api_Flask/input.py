from flask import Flask

app = Flask(__name__)

@app.route("/frame", methods=['POST'])
def frame():
  return "hello world"
