from flask import Flask,render_template,request,jsonify
from paraser import *
from telegram import *

application = Flask(__name__)

@application.route("/")
def hello():

	staticticks = get_statisticks()
	ip_addr = request.remote_addr
	user_agent = request.user_agent
	data = request.data
	print(data)
	return render_template('main.HTML',staticticks=staticticks)

if __name__ == "__main__":
	application.run(host='0.0.0.0')