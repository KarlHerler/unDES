import os

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
  return render_template('index.html')

@app.route("/key", methods=['GET', 'POST'])
def key():
  returner = ""
  if (request.method=='POST'):  
    returner = returner +  handleReport((request.form["result"].lower()=="true")) + "\n"
    #returner = returner + request.method+"\n"
  
  return returner + "get keys, TBD"

@app.route("/report", methods=['GET', 'POST'])
def report():
  return handleReport(request.method=='POST')

def handleReport(r):
  #return request.form["key"]
  if r: return "shit something found!"
  else: return "no key found, thanks for playing"


if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
