#### Using regular expressions

import re
re.search(r"(hello|hey|hi)", "hey there!") is not None
re.search(r"(hello|hey|hi)", "which one?") is not None
re.search(r"\b(hello|hey|hi)\b", "hey there!") is not None
re.search(r"\b(hello|hey|hi)\b", "which one?") is not None

#### Using regex for entity recognition
pattern = re.compile('[A-Z]{1}[a-z]*')
message = """
Mary is a friend of mine,
she studied at Oxford and
now works at Google"""

pattern.findall(message) 

#### Word vectors

## conda install -c conda-forge spacy=2.0.11
## python -m spacy download en_core_web_md

import spacy
# python -m spacy download en_core_web_md
nlp = spacy.load('en_core_web_md')

print(nlp.vocab.vectors_length)
doc = nlp(u'hello can you help me?') 
for token in doc:
    print("{} : {}".format(token, token.vector[:3]))
print(doc[0].vector)


doc = nlp('cat')

print(doc.similarity(nlp('can')))

print(doc.similarity(nlp('dog')) )

#### Intents and classification (to be finished)

#### Entity extraction

import spacy
nlp = spacy.load('en')
doc = nlp("what kind of aircraft is used on a flight from Cleveland to Dallas")
ents = doc.ents
for ent in ents:
    print(ent.text, ent.label_)

import re
## Roles
pattern_1 = re.compile('.* from (.*) to (.*)')
pattern_2 = re.compile('.* to (.*) from (.*)')

## Dependency parsing
doc = nlp('a flight to Shanghai from Singapore')
sh, sg = doc[3], doc[5]

list(sh.ancestors)
list(sg.ancestors)

## Shopping example
doc = nlp("let's see that jacket in red and some blue jeans")

items = [doc[4], doc[10]]  # [jacket, jeans]
colors = [doc[6], doc[9]]  # [red, blue]
for color in colors:
    for tok in color.ancestors:
        if tok in items:
            print("color {} belongs to item {}".format(color, tok))
            break

#### Robust NLU with Rasa

## Rasa NLU

# Rasa data format

from rasa_nlu.training_data import load_data
training_data = load_data('/Users/fzhang/Documents/projects/rasa_nlu/data/examples/rasa/demo-rasa.json')
import json
print(json.dumps(training_data.entity_examples[0].data, indent=2))

# Interpreters

from rasa_nlu.model import Trainer
from rasa_nlu import config

message = "I'm looking for a Mexican restaurant in the North of town"
trainer = Trainer(config.load("/Users/fzhang/Documents/projects/rasa_nlu/sample_configs/config_spacy.yml"))
interpreter = trainer.train(training_data)
interpreter.parse(message)

message = "Tell me a Italian restaurant in the South"
interpreter.parse(message)

git clone https://github.com/RasaHQ/rasa_nlu.git
cd rasa_nlu
pip install -r requirements.txt
pip install -e .

python -m rasa_nlu.train    --config sample_configs/config_spacy.yml    --data data/examples/rasa/demo-rasa.json    --path projects

python -m rasa_nlu.server --path projects

# curl -X POST localhost:5000/parse -d '{"q":"I am looking for Mexican food"}' | python -m json.tool
# curl -XPOST localhost:5000/parse -d '{"q":"hello there"}'

