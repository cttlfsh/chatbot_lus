from def_structures import JSONEntity, CommonExs

import json

training_file = "../intents_db/NLSPARQL.train.data"
testing_file = "../intents_db/NLSPARQL.train.data"
training_lab = "../intents_db/NLSPARQL.train.utt.labels.txt"
testing_lab = "../intents_db/NLSPARQL.test.utt.labels.txt"

example = CommonExs(None, None, [])
entity = JSONEntity(0, 0, None, None)

entities = []
to_be_proc = []

sentence = ""

def intent_processing(intent):
	if (intent == "actor"):
		intent = "actor_name"
	elif (intent == "director"):
		intent = "director_name"
	if (" " in intent):
		intent = intent.replace(" ", "_&&_")
	
	return intent


'''

I have to process both training and label files to
obtain necessary information, namely:
	
	1] "text" --> the whole sentence
	2] "intent" --> the label
	3] "entities" --> some information, in particular:
		a] "start" e "end" --> starting and ending position of the
			entity value
		b] "value" --> actual value of the entity
		c] "entity" --> IOB Tag of the value

'''

with open(training_file) as tf:
	with open(training_lab) as tl:
		for line in tf.readlines():
			if line == "\n":
				if entity.can_add == True:
					entities.append(entity)

				### Read the label (intent)
				label = tl.readline()
				### Set the text of the entity
				example.text = sentence
				### Set the intent of the entity
				example.intent = intent_processing(label.split("\n")[0])

				### For each entity, find start and end position
				### and append it
				for e in entities:
					e.find_boundaries(example.text)
					example.entities.append(e)

				to_be_proc.append(example)
				### Reinstanciate for the next sentence
				example = CommonExs(None, None, [])
				entity = JSONEntity(0, 0, None, None)
				entities = []
				sentence = ""

			else:
				word = line.split("\t")[0]
				tag = line.split("\t")[1][:-1]
				if (sentence == ""):
					sentence = word
				else:
					sentence = sentence + " " + word 
				#print(tag[0])
				if(tag[0] == "I"):
					if entity.entity is not None:
						if entity.entity == tag[2:]:
							entity.value = entity.value + " " + word
							entity.can_add = True

				elif (tag[0] == "O"):
					if entity.entity is not None:
						entities.append(entity)
						entity = JSONEntity(0, 0, None, None)

				elif (tag[0] == "B"):
					if entity.entity is not None:
						entities.append(entity)
						entity = JSONEntity(0,0,word, tag[2:])
					else:
						entity.entity = tag[2:]
						entity.value = word
						entity.can_add = True



processed = {
		"rasa_nlu_data" : {
			"common_examples": [example.get_json() for example in to_be_proc],
			"entity_examples": [],
			"intent_examples": []
		}
}

with open("../files/nlu_data.json", "w") as j:
    json.dump(processed, j)
