from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def index():
	return "Flask App!"

# @app.route("/hello/<name>/")
# def hello(name):


@app.route('/hello/<name>')
def hello_name(name):
	return render_template('test.html',name=name)
   # return 'Hello %s!' % name

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True, port=1314)