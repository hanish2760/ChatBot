import requests
import pandas as pd
import xlrd

#from QuestionRetrieval import  get_response


def find_IssueKey(entities):
    entities=list()
    issueKeyDict=dict()
    entities.append('status')
    entities.append('review')
    entities.append('handling')
    data=pd.read_excel(r'./data/forRasaNluCheque.xlsx')
    df=pd.DataFrame(data)
    for index,row in df.iterrows():
        summary=str(row['Summary'])
        summary=summary.lower()
        issueKey=row['Issue key']
        if(any(entity in summary for entity in entities)):
            print("*"+row)
    #df2=df[df['Summary'].isin(['status','review','handling'])]
    print(df)
    pass


from rasa_nlu.model import Interpreter


def test_bot():
    nlu_model = Interpreter.load('./tests/models/default/chat_bot')
    while(True):
        user_message = str(input("YOU to BOT :"))
        parsing=nlu_model.parse(user_message)
#parsng has all the intent info and entities info
        print('Intent : ' + parsing["intent"]["name"])
        intent=parsing["intent"]["name"]
        list_of_entities=parsing["entities"]
        entities=""
        for entity in list_of_entities:
            print("Entity Value : " +entity['value'])
            entities+=entity['value']

        if intent== "Intentcheque":
            import QuestionRetrieval
            # if(len(entities)>0):
            #     answere=QuestionRetrieval.get_response(entities=entities)
            # else:
            #     answere=QuestionRetrieval.get_response(query=user_message)
            answere=QuestionRetrieval.get_response(user_message,entities)
            print("Bot : "+answere)
        elif intent == "greet" :
            print("Bot: Hello")

        elif intent == "affirm":
            print("Bot : Ok")

        elif intent == "goodbye":
            print("Bot : Bye")

        else:
            print("Bot :  Sry i dint get you")
from rasa_nlu.training_data import load_data

training_data = load_data("training_data.json")
def synnonym(word):
    synms=training_data.entity_synonyms
    pass

def chat():
    try:
        user_message =str(input("YOU to BOT :"))
        #change port
        response = requests.get("http://localhost:5000/parse",params={"q":user_message})
        response = response.json()
        #response = response["topScoringIntent"]
        intent = response.get("intent")
        intent=intent['name']
        print('intent is '  + intent)
        entities = response.get("entities")
        ents=""
        for item in entities:
            ents+=item['value']
            ents+='  ,'
        print(" entities are " + ents)
        #write your code for the intent indentified.
        if intent== "Intentcheque":
            #key=find_key(entities)
            print("Bot : ")
            import QuestionRetrieval
            QuestionRetrieval.get_response(ents)

        elif intent == "greet" :
            print("Hello")
            #response_text = gst_info(entities)
        elif intent == "affirm":
            print("intent indentified as affirm")
            #response_text = gst_query(entities)
        elif intent == "goodbye":
            print("Bye!")
            #response_text = gst_query(entities)
        else:
            print("random")
            #response_text = get_random_response(intent)
        return
    except Exception as e:
        print(e)
        return


# To chat when the bot is run on a server

#while(True):
#    chat()

#to load bot and run in script
#test_bot()
synnonym("cheque")



