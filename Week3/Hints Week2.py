#### Virtual assistants and  accessing data
## SQLite with Python

import sqlite3
conn = sqlite3.connect('hotels.db')
c = conn.cursor()
c.execute("DROP TABLE hotels")
c.execute("CREATE TABLE IF NOT EXISTS hotels(name text, price text, location text, stars int)")
c.execute("INSERT INTO hotels(name, price, location, stars) VALUES('Hotel for Dogs', 'mid', 'east', 3)")
c.execute("INSERT INTO hotels(name, price, location, stars) VALUES('Hotel California', 'mid', 'north', 3)")
c.execute("INSERT INTO hotels(name, price, location, stars) VALUES('Grand Hotel', 'hi', 'south', 5)")
c.execute("INSERT INTO hotels(name, price, location, stars) VALUES('Cozy Cottage', 'lo', 'south', 2)")
c.execute("INSERT INTO hotels(name, price, location, stars) VALUES('Bens BnB', 'hi', 'north', 4)")
c.execute("INSERT INTO hotels(name, price, location, stars) VALUES('The Grand', 'hi', 'west', 5)")
c.execute("INSERT INTO hotels(name, price, location, stars) VALUES('Central Rooms', 'mid', 'center', 3)")
c.execute("commit")

c.execute("SELECT * FROM hotels")
print(c.fetchall())

## Exploring a DB with  natural language
# Parameters from text
# Import necessary modules
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config

# Create a trainer that uses this config
trainer = Trainer(config.load("config_spacy.yml"))

# Load the training data
training_data = load_data('demo-rasa.json')

# Create an interpreter by training the model
interpreter = trainer.train(training_data)

## Catching negations
import spacy
nlp = spacy.load("en_core_web_md")
doc = nlp('not sushi, maybe pizza?')
indices = [1, 4]
ents, negated_ents = [], []
start = 0
for i in indices:
    phrase = "{}".format(doc[start:i])
    if "not" in phrase or "n't" in phrase: 
        negated_ents.append(doc[i])
        print(negated_ents) #有问题！
    else:
        ents.append(doc[i])
        print(ents)
    start = i

print(ents)
print(negated_ents)
