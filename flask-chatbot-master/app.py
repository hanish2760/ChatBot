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
		answere=dict()

		response=QuestionRetrieval.get_response(user_message,entities)
		answere['ans']=response
		answere['qr']="Is this what You were looking for ? "
		answere['intent']=intent
		return(answere)
		#print("Bot : " + answere)
	elif intent == "greet":
		answere=dict()
		answere['ans']="Hello"
		answere['qr']=""
		answere['intent']=intent
		return answere
		#print("Bot: Hello")

	elif intent == "affirm":
		answere = dict()
		answere['ans'] = "ok"
		answere['qr'] = ""
		answere['intent'] = intent
		return answere

		#print("Bot : Ok")

	elif intent == "goodbye":
		answere = dict()
		answere['ans'] = "Bye"
		answere['qr'] = ""
		answere['intent'] = intent
		return answere

		#print("Bot : Bye")

	else:
		#ee mama repeatu
		answere = dict()
		answere['ans'] = "Sorry I couldn't get you. Could you be more specific about the isuuue."
		answere['qr'] = ""
		answere['intent'] = intent
		return answere


app = Flask(__name__)
@app.route("/")

def hello():
	return render_template('chat1.html')

@app.route("/ask", methods=['POST','GET'])
def ask():
	message = str(request.form['chatmessage'])
	response=get_response(message)
	intent=response['intent']
	return jsonify({"status": "ok", "answer": response['ans'],"quick_replies":response['qr'],"intent":intent})
		# while True:
		# print bot_response

if __name__ == "__main__":
    app.run(debug=False)

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