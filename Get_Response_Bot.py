
from rasa_nlu.model import Interpreter
nlu_model = Interpreter.load('./tests/models/default/chat_bot')

def get_response(user_message):
	parsing = nlu_model.parse(user_message)
	# parsng has all the intent info and entities info
	#print('Intent : ' + parsing["intent"]["name"])
	intent = parsing["intent"]["name"]
	list_of_entities = parsing["entities"]
	entities = ""

	for entity in list_of_entities:
		#print("Entity Value : " + entity['value'])
		entities += entity['value']

	if intent == "Intentcheque":
		import QuestionRetrieval
		if (len(list_of_entities) >= 3):
			if (len(entities) > 0):
				answere = QuestionRetrieval.get_response(entities)
		else:
			answere=" I need more info..but this is what I could best find..."
			answere+= QuestionRetrieval.get_response(user_message)
		return(answere)
		#print("Bot : " + answere)
	elif intent == "greet":
		return "Hello!"
		#print("Bot: Hello")

	elif intent == "affirm":
		return "Ok"
		#print("Bot : Ok")

	elif intent == "goodbye":
		return "Bye!"
		#print("Bot : Bye")

	else:
		return "Sry i dint get you"
		print("Bot :  Sry i dint get you")