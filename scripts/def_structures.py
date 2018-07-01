class JSONEntity():
	def __init__(self, start, end, value, entity):
		self.start = start
		self.end = end
		self.value = value
		self.entity = entity
		self.can_add = False

	def get_json(self):
		return {
			"start": self.start,
			"end": self.end,
			"value": self.value,
			"entity": self.entity
		}

	def find_boundaries(self, text):
		try:
			start = text.index(self.value)
			end = start + len(self.value)
			self.start = start
			self.end = end
		except:
			print (text)
			print (self.value)
			print(text.index(self.value))

class CommonExs(object):
	"""docstring for CommonExs"""
	def __init__(self, text, intent, entities):
		self.text = text
		self.intent = intent
		self.entities = entities

	def get_json(self):
		return {
			"text": self.text,
			"intent": self.intent,
			"entities": [entity.get_json() for entity in self.entities]
		}