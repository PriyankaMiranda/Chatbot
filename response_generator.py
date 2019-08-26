import train_bot
import yaml
import utils
import constants

class response_generator_class:
	def __init__(self, socket,message):
	    """
	    Initialize the response gsenerator object.
	    Args:
	        socket 
	        message
	    Returns:
	        void
	    """
	    self.socket = socket
	    self.message = message

	def conversation_bot(self):
		conv_bot=train_bot.init_train()
		return self.conversation_bot_response(conv_bot)

	def conversation_bot_response(self,chatbot):
		response=chatbot.get_response(self.message)
		return str(response)


	def assistance_bot(self):
		assist_bot,user_option_vals=train_bot.train_assistance_bot()
		print("Our assistence bot is available now.")
		options=utils.get_options(user_option_vals)
		generate_response(assist_bot,"shopping assistance",options,constants.USER_OPTIONS_COUNT)

	def map_bot(self,reply, options):
		# carries out the fuction on basis of the selected option 
		return 'Under construction'




	def generate_response(self,chatbot,reason,options,disp_count):
		data='Hello'
		print("Type exit to leave")
		if (not options==None):
			n=0
			while (not data.lower()=="exit"):
				sub_set_options= utils.add_lists(options[n:n+disp_count],constants.EXTRA_OPTIONS)
				print(sub_set_options)
				print("You:")
				data=input()
				if data=='other':
					n=n+disp_count
					if n >= len(options):
						n=0
					continue

				response=map_bot(data,options)
				print("Bot:")
				print(response)		
		while (not data.lower()=="exit"):
			# Get a response to an input statement
			response=chatbot.get_response(data)
			print("Bot:")
			print(response)
			print("You:")
			data=input()
			if (str(data).lower()=='help'):
				assistance_bot()
				return
		print("Want to know more about our "+reason+" services? Share a few details for a better experience.")
		print("Name:")
		name=input()
		print("Email id:")
		email_id=input()
		print("Mobile no:")
		mobile_no=input()
		print("Thank you for conversing with our bot!")