
from flask import Flask, render_template
from flask_socketio import SocketIO
import main 
from train_bot import train_bot_class 
import numpy as np
from pymongo import MongoClient
app = Flask(__name__)
app.config['SECRET_KEY'] = '123##'
socketio = SocketIO(app)
bots=train_bot_class()


client = MongoClient("mongodb://chatbot_admin:qwerty123@127.0.0.1:27017") #host uri
db = client.mymongodb #Select the database
chatbot_dbs = db.chatbot_db


@app.route('/')
def sessions():
	return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
	print('message was received!!!')

def get_reply(query):
	return str(bots.conversation_bot.get_response(query))

@socketio.on('Update db')  
def update_db (user):   
	chatbot_dbs.insert(user)	

@socketio.on('Get details')
def get_details(value, methods=['GET', 'POST']):
	print("-----------------------")
	print(value)
	print("----------------------")
	socketio.emit('display options', value, callback=messageReceived)


@socketio.on('Get options')
def send_options(value, methods=['GET', 'POST']):
	if (not bool(value)):
		user_options=bots.user_options()
		user_options=user_options["conversations"]
		socketio.emit('display options', user_options, callback=messageReceived)
	else:
		user_options=dict()
		user_options=value[value['user_options']]
		socketio.emit('display options', user_options, callback=messageReceived)

@socketio.on('Chat Event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
	print('received my event: ' + str(json))
	if (json["type"]=='intro'):
		json['user_options']={}
		socketio.emit('response', json, callback=messageReceived)
		return
	socketio.emit('response', json, callback=messageReceived)


if __name__ == '__main__':
	socketio.run(app ,port=5000, debug=True, host='0.0.0.0')