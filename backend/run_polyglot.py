from polyglot.text import Text
from collections import Counter



def run_polyglot(txt):
	assert type(txt) == str
	tru = Text(txt, hint_language_code='Eng')
	entities_en = tru.entities

	ten = Text(txt, hint_language_code='Rus')
	entities_ru = ten.entities

	temp = []
	for sent in tru.sentences:
  		for entity in sent.entities:
  			if entity.tag == 'I-LOC':
    			temp.append(str(entity))


	if len(Counter(temp)) !=0:
		entities_dict = Counter(temp)
	else:
		temp = []
		for sent in ten.sentences:
	  		for entity in sent.entities:
	  			if entity.tag == 'I-LOC':
	    			temp.append(str(entity))
	entities_dict = Counter(temp)
	return entities_dict


txt = open("TICKET.txt", "r").read()
print(txt)
dictr = run_polyglot(txt)
print(dictr)