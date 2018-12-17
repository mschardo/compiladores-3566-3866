import re
from Engine import Engine
from Event import Event

# Nível de abstração 0
def readFile(file_path):
	try:
		file = open(file_path, 'r')
		for line in file.readlines():
			print("readFile \tLine: " + line)
			yield Event("Linha", {'line': line}, engine='lexer')
	except FileNotFoundError:
		print("File not found {}.".format(file_path))

# Nível de abstração 1
def readLine(line):
	chars_list = list(line)
	for char in chars_list:
		yield Event("Char", {'char': char}, engine='lexer')
		
# Nível de abstração 2 a 4
def charClassifier(char):
	if(char in [' ', '\t']):
		tipo = 'descartável'
	elif(char != '\n'):
		tipo = 'útil'
	else:
		tipo = 'controle'

	if re.match(r'[a-zA-Z]', char):
		classe = 'letra'
	elif re.match(r'[0-9]', char):
		classe = 'dígito'
	elif char in [' ', '\t']:
		char = 'espaço'
		classe = 'delimitador'
	elif char == '\n':
		char = 'EOL'
		classe = 'controle'
	else:
		classe = 'especial'

	print("charClassifier \tChar: " + char + "\t\tTipo: " + tipo + "\tClasse: " + classe)
	yield Event("ClassificaçãoDeChar", {'char': char, 'char_type': tipo, 'char_class': classe}, engine='lexer')

# Nível de abstração 5 e 6
def tokenizer(char, char_type, char_class, state, token, engine):
	transition = {
		'A': {'letra': 'B','dígito': 'C', 'especial': 'D'},
		'B': {'letra': 'B','dígito': 'B'},
		'C': {'dígito': 'C'},
		'D': {}
	}
	states = {
    	'A': {'final': False},
    	'B': {'final': True, 'tipo':'texto'},
    	'C': {'final': True, 'tipo':'inteiro'},
    	'D': {'final': True, 'tipo':'especial'},
	}

	state = engine.parameters['state']
	if char_type in ['controle', 'descartável']:
		if states[state]['final']:
			engine.parameters['state'] = 'A'
			engine.parameters['token'] = ''
			yield Event("Token", {'token': token, 'token_type': states[state]['tipo']}, engine='lexer')
		else:
			if state != 'A':
				raise SyntaxError("Invalid token: {}".format(token))
	elif char_type == 'útil' and char_class == 'especial':
		if states[state]['final']:
			engine.parameters['state'] = 'A'
			engine.parameters['token'] = ''
			yield Event("Token", {'token': token, 'token_type': states[state]['tipo']}, engine='lexer')
		state = transition[engine.parameters['state']][char_class]
		token = char
		yield Event("Token", {'token': token, 'token_type': states[state]['tipo']}, engine='lexer')
		engine.parameters['state'] = 'A'
		engine.parameters['token'] = ''
	else:
		engine.parameters['token'] = token + char
		if char_class in transition[state].keys():
			engine.parameters['state'] = transition[state][char_class]
		else:
			raise SyntaxError("Invalid token: {}".format(token))

def tokenClassifier(token, token_type, token_list):
	palavras_reservadas = ["END", "LET", "FN", "SIN", "COS", "TAN", "ATN", "EXP", "ABS", "LOG", "SQR", "INT", "RND", "READ", "DATA", "PRINT", "GOTO", "GO", "TO", "IF", "THEN", "FOR", "TO", "STEP", "NEXT", "DIM", "DEF", "FN", "GOSUB", "RETURN", "REM", ">=", "<>", "<="]

	print("\nToken: " + token + "\t Tipo: " + token_type)

	if token in palavras_reservadas:
		print("Token: " + token + "\t Classe: reservada")
		token_list.append({'token': token, 'classe': 'reservada'})
	else:
		for char in token:
			if re.match(r'[a-zA-Z]', char):
				print("Token: " + char + "\t Classe: letter")
				token_list.append({'token': char, 'classe': 'letter'})
			elif re.match(r'[0-9]', char):
				print("Token: " + char + "\t Classe: digit")
				token_list.append({'token': char, 'classe': 'digit'})
			else:
				print("Token: " + char + "\t Classe: especial")
				token_list.append({'token': char, 'classe': 'especial'})

filename = "../programas_teste/fibbonacci.bs"
engines = {}

engines['lexer'] = Engine({'Arquivo': readFile, 'Linha': readLine, 'Char': charClassifier, 'ClassificaçãoDeChar':tokenizer, 'Token': tokenClassifier}, Event('Arquivo', {'file_path': '../programas_teste/bubbleSort.bs'}), parameters={'state': 'A', 'token': '', 'token_list': []})
engines['lexer'].parameters['engine'] = engines['lexer']

engines['lexer'].fetch_exhaustive(engines)