import os

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
  return render_template('index.html')

@app.route("/key")
def key():
  if request.method=='POST': return handleReport(true)+"\n get keys"
  return "get keys, TBD"

@app.route("/report/")
def report():
  return handleReport(request.method=='GET')

def handleReport(r):
  if r: return "shit something found!"
  else: return "no key found, thanks for playing"

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
