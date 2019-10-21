
def multiply(a, b):
	return a*b


directions = ['north', 'south', 'east']
verbs = ['go', 'kill', 'eat']
stops = ['the', 'in', 'of']
nouns = ['bear', 'princess']

def scan(direction):
	result = []
	words = direction.split()
	for word in words:
		try:
			word = int(word)
			if isinstance(word, int):
				pair = ('number', word)
				result.append(pair)
		except ValueError:
			if word in directions:
				pair = ('direction', word)
				result.append(pair)
			elif word in verbs:
				pair = ('verb', word)
				result.append(pair)
			elif word in stops:
				pair = ('stop', word)
				result.append(pair)
			elif word in nouns:
				pair = ('noun', word)
				result.append(pair)
			else:
				pair = ('error', word)
				result.append(pair)
	return result

print(scan('123'))
