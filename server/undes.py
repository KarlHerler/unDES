import os

from flask import Flask, render_template, request
from Key import Key
from Metrics import Metrics
import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
k = Key()
m = Metrics()


app = Flask(__name__)

@app.route("/")
def hello():
  #warning, middleware doing domain level stuff
  return render_template('index.html', current=m.current())


@app.route("/key", methods=['GET', 'POST'])
def key():
  if (request.method=='POST'): handleReport((request.form["found"].lower()=="true"))
  return k.get()


@app.route("/report", methods=['POST'])
def report():
  return handleReport(request.form["found"].lower()=="true")


def handleReport(r):
  return k.report(request.form["range"], r, request.form["key"])

if __name__ == "__main__":
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)
