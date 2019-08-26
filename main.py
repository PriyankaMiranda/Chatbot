from response_generator import response_generator_class

def chatterbot(socket,message):
	rg=response_generator_class(socket,message)
	return rg.conversation_bot()

if __name__=="__main__":
	chatterbot()
	