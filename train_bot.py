from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from keras.models import model_from_yaml
import constants
import yaml
import os 
from glob import glob
class train_bot_class:
	def __init__(self):
		self.yaml_file_loc="/home/office/Documents/Priyanka/implementations/chatbot/yaml_train"
		self.yaml_ext="*.yaml"
		self.assistance_file="/home/office/Documents/Priyanka/implementations/chatbot/training_assistance.yaml"
		self.conversation_bot=self.conv_bot_train()
		# self.assistance_bot=self.train_assist_bot()
	def conv_bot_train(self):
		all_files = [file
		for path, subdir, files in os.walk(self.yaml_file_loc)
		for file in glob(os.path.join(path, self.yaml_ext))]

		chatbot = ChatBot('Converstion bot')
		# Create a new trainer for the chatbot
		trainer = ChatterBotCorpusTrainer(chatbot)
		# Train the chatbot with the yaml files
		for file in all_files:
			try:
				trainer.train(file)
			except:
				continue
		return chatbot

	def user_options(self):
		with open(self.assistance_file, 'r') as stream:
			data= yaml.safe_load(stream)
			# try:
			# 	data= yaml.safe_load(stream)
			# except:
			# 	print(str(self.assistance_file)+" file not read or error in format.")
		return data