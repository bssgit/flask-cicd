from flask import Flask

app = Flask(__name__)

@app.route("/",methods=["GET"])

def root():
  return "this is flask web for cicd"

app.run(host="0.0.0.0", port=4000, debug=True)


