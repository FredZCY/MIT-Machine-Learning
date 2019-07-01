# Import necessary modules from RASA
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config

# Create a trainer that uses this config
trainer = Trainer(config.load("config_spacy.yml"))

# Load the training data
training_data = load_data("stock-data.json")

# Create an interpreter by training the model
interpreter = trainer.train(training_data)

# Import necessary modules from iexfinance
from iexfinance.stocks import Stock, get_historical_intraday
from datetime import datetime

# Define function to extract intent
def intent_extraction(message):
    return interpreter.parse(message)["intent"]["name"]

# Define function to extract entities
def entity_extraction(message):
    entities = interpreter.parse(message)["entities"]
    parameters = {}
    for ent in entities:
        parameters[ent["entity"]] = str(ent["value"])
    return parameters

# Define functions to obtain current price, open/close price, volume of a specified stock
def current_price(parameters):
    return Stock(parameters["company"], token = "sk_da231175d2cb425bbf943b1946966cfb").get_price()

def open_price(parameters):
    date = datetime(int(parameters["year"]),int(parameters["month"]),int(parameters["day"]))
    op = get_historical_intraday(parameters["company"], date, output_format = 'pandas', token = "sk_da231175d2cb425bbf943b1946966cfb")["open"][0]
    return op

def close_price(parameters):
    date = datetime(int(parameters["year"]),int(parameters["month"]),int(parameters["day"]))
    cp = get_historical_intraday(parameters["company"], date, output_format = 'pandas', token = "sk_da231175d2cb425bbf943b1946966cfb")["close"][0]
    return cp;

def volume(parameters):
    date = datetime(int(parameters["year"]),int(parameters["month"]),int(parameters["day"]))
    vl = get_historical_intraday(parameters["company"], date, output_format = 'pandas', token = "sk_da231175d2cb425bbf943b1946966cfb")["volume"][0]
    return vl;

# Define the states
INIT = 0 
FUNC = 1
CURRENT_PRICE = 2
HISTORY_DATA_open = 3
HISTORY_DATA_close = 4
HISTORY_DATA_volume = 5
END = 6

# Define the potential responses
responses = [
        "Welcome! My name is Coco and I can share stock information with you.",
        "I can tell you: \n  1) The current price\n  2) The historical data:\n        1. the open/close price\n        2. the volume",
        "Got it! The current price of {} is {}.",
        "U wanna know the open price! It's {}.",
        "The close price on that day was {}.",
        "On that day, the volume was {}.",
        "You are always welcome, my lord/lady!",
        "Au Revoir! My friend @_@",
        "Thank you for your using! ^_^"
        ]

import random

# Define the policy rules
policy_rules = {
    (INIT, "greet"): (FUNC, responses[0]),
    (FUNC, "greet"): (FUNC, responses[0]),
    (FUNC, "intro"): (FUNC, responses[1]),
    
    (FUNC, "current_price"): (CURRENT_PRICE, responses[2]),
    # Able to show current price for multiple-time queries
    (CURRENT_PRICE, "current_price"): (CURRENT_PRICE, responses[2]),
    (CURRENT_PRICE, "history_data_open"): (HISTORY_DATA_open, responses[3]),
    (CURRENT_PRICE, "history_data_close"): (HISTORY_DATA_close, responses[4]),
    (CURRENT_PRICE, "history_data_volume"): (HISTORY_DATA_volume, responses[5]),
    
    (FUNC, "history_data_open"): (HISTORY_DATA_open, responses[3]),
    (FUNC, "history_data_close"): (HISTORY_DATA_close, responses[4]),
    (FUNC, "history_data_volume"): (HISTORY_DATA_volume, responses[5]),
    
    (HISTORY_DATA_open, "history_data_close"): (HISTORY_DATA_close, responses[4]),
    (HISTORY_DATA_open, "history_data_volume"): (HISTORY_DATA_volume, responses[5]),
    (HISTORY_DATA_close, "history_data_open"): (HISTORY_DATA_open, responses[3]),
    (HISTORY_DATA_close, "history_data_volume"): (HISTORY_DATA_volume, responses[5]),
    (HISTORY_DATA_volume, "history_data_open"): (HISTORY_DATA_open, responses[3]),
    (HISTORY_DATA_volume, "history_data_close"): (HISTORY_DATA_close, responses[4]),
    
    # Random choose the sentences for ending
    (CURRENT_PRICE, "end"):(FUNC, random.choice([responses[6], responses[7], responses[8]])),
    (HISTORY_DATA_open, "end"):(FUNC, random.choice([responses[6], responses[7], responses[8]])),
    (HISTORY_DATA_close, "end"):(FUNC, random.choice([responses[6], responses[7], responses[8]])),
    (HISTORY_DATA_volume, "end"):(FUNC, random.choice([responses[6], responses[7], responses[8]])),
    (FUNC, "end"):(FUNC, random.choice([responses[6], responses[7], responses[8]]))
}

# Define the main respond function
def respond(policy_rules, state, message):

    entities = entity_extraction(message)

    if intent_extraction(message) == "greet":
        newstate = policy_rules[(state,intent_extraction(message))][0]
        response = policy_rules[(state,intent_extraction(message))][1]
    if intent_extraction(message) == "intro":
        newstate = policy_rules[(state,intent_extraction(message))][0]
        response = policy_rules[(state,intent_extraction(message))][1]
    if intent_extraction(message) == "current_price":
        newstate = policy_rules[(state,intent_extraction(message))][0]
        response = policy_rules[(state,intent_extraction(message))][1].format(entities["company"],current_price(entities))
    if intent_extraction(message) == "history_data_open":
        newstate = policy_rules[(state,intent_extraction(message))][0]
        response = policy_rules[(state,intent_extraction(message))][1].format(open_price(entities))    
    if intent_extraction(message) == "history_data_close":
        newstate = policy_rules[(state,intent_extraction(message))][0]
        response = policy_rules[(state,intent_extraction(message))][1].format(close_price(entities))       
    if intent_extraction(message) == "history_data_volume":
        newstate = policy_rules[(state,intent_extraction(message))][0]
        response = policy_rules[(state,intent_extraction(message))][1].format(volume(entities))       
    if intent_extraction(message) == "end":
        newstate = policy_rules[(state,intent_extraction(message))][0]
        response = policy_rules[(state, intent_extraction(message))][1]
        
    return newstate, response


def send_message(policy_rules, state, message):
    new_state, response = respond(policy_rules, state, message)
    return new_state, response


def send_messages(messages):
    state = INIT
    for msg in messages:
        state, response = send_message(policy_rules, state, msg)
 
# Only for testing    
"""
send_messages(
    [
        "Hi",
        "What can you do?",
        "Could you please tell me the current price of Nike?",
        "And what about the open price of Facebook on 2019-03-05",
        "Please show me the close price of Alibaba on 2019-03-06",
        "Now show the volume of Apple on 2019-03-07",
        "Thanks, bye",
        "Oh! I forgot, please show me the current price of Facebook",
        "Farewell"
    ]
)
"""

# Import the necessary wechat module
from wxpy import *

# Initialize the Bot
bot = Bot()

# Search the specified Wechat account
my_friend = bot.friends().search('Stockbot Coco')[0]

@bot.register(my_friend, TEXT)

# Reply messages sent by my_friend Stockbot Coco
def reply_message(message):
    # my_friend.send('Received: {} ({})'.format(message.text, message.type))
    msg=message.text
    state = FUNC
    state, response = send_message(policy_rules, state, msg)
    my_friend.send(response)










