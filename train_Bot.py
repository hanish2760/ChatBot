from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
from rasa_core.agent import Agent
import requests
import json

def test_nlu_interpreter():
    #training_data = load_data("data/nlu_data.md") # the training data
    training_data = load_data("data/training_data.json")  # the training data
    trainer = Trainer(config.load("nlu_config.yml")) #the config file
    #trainer=Trainer(config.load("new_nlu_config.json"))
    interpreter = trainer.train(training_data)
    test_interpreter_dir = trainer.persist("./tests/models",fixed_model_name = 'chat_bot')
    test_interpreter_dir = trainer.persist(".flask-chatbot-master/tests/models", fixed_model_name='chat_bot')

    return interpreter

def joke_bot(interpreter):
    while (True):
        msg = input('You :')
        parsing = interpreter.parse(msg)

        if (str(parsing['intent']['name']) == 'joke'):
            request = json.loads(
                requests.get("https://api.chucknorris.io/jokes/random").text
            )  # make an api call
            joke = request["value"]  # extract a joke from returned json response
            print('joke - ' + str(joke))
    """
    loaded = Agent.load("./tests/models/default")
    i2=loaded.interpreter
    parse2=i2.parse("hello") """

    assert parsing["intent"]["name"] == "greet"
    assert test_interpreter_dir


interpreter=test_nlu_interpreter()
#joke_bot(interpreter)

