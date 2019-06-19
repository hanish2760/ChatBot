from flask import Flask, render_template, request, jsonify
import os
import requests

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
		# if (len(entities) > 0):
		# 	answere = QuestionRetrieval.get_response(entities)
		# else:
		# 	answere = QuestionRetrieval.get_response(user_message)
		answere=QuestionRetrieval.get_response(user_message,entities)
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


app = Flask(__name__)
@app.route("/")

def hello():
	return render_template('chat1.html')

@app.route("/ask", methods=['POST','GET'])
def ask():
	message = str(request.form['chatmessage'])
	if message == "save":
	    return jsonify({"status":"ok", "answer":"Brain Saved"})
	elif message == "reload":
		return jsonify({"status":"ok", "answer":"Brain Reloaded"})
	elif message == "quit":
		exit()
		return jsonify({"status":"ok", "answer":"exit Thank You"})

	# kernel now ready for use
	else:
		#chabot code
		response=get_response(message)
		# response = requests.get("http://localhost:5000/parse", params={"q": message})
		# response = response.json()
		# intent = response.get("intent")
		# intent = intent['name']
		# entities = response.get("entities")
		# ents = ""
		# for item in entities:
		# 	ents += item['value']
		# 	ents += '  '
		# if intent == "Intentcheque":
		# 	# key=find_key(entities)
		# 	import QuestionRetrieval
		# 	ans=str(QuestionRetrieval.get_response(ents))+ "..you might find your issue here."
		# elif intent == "greet":
		# 	ans="Hello"
		# # response_text = gst_info(entities)
		# elif intent == "affirm":
		# 	ans="Okay!"
		# elif intent == "badbye":
		# 	ans="Bye!"
		# # response_text = gst_query(entities)
		# else:
		# 	ans="Sorry I dint get You "
	return jsonify({"status": "ok", "answer": response})
		# while True:
		# print bot_response

if __name__ == "__main__":
    app.run(debug=False)
