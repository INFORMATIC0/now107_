from flask import Flask, request
from os.path import exists

app = Flask(__name__)

@app.route("/")
def hello():
    if not exists('data'):
    	open('data','w').write('[]')
    if not exists('version'):
    	open('version','w').write('1')
    return open('data', 'r').read()

@app.route("/admin")
def admin():
    now = request.args['text']
    open('data','w').write(now)
    return ""
@app.route("/adminv")
def adminv():
    now = request.args['version']
    open('version','w').write(now)
    return ""
@app.route("/version")
def ver():
	return open('version', 'r').read()
if __name__ == "__main__":
    app.run()