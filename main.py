import sys
from lexer import lex
from wordy import gre, les, neq, eq, greeq, leseq
filename = sys.argv[1]
vars = {}
file = open(filename)
def runline(parsed):
	options = {
		"vset":vset,
		"print":disp,
		"if":condit
	}
	options[parsed['operand']](parsed['args'])
def tryInt(veer):
	ver = 0
	try:
		ver = int(veer)
	except:
		ver = veer	
	return ver
class CompileError(Exception):
	pass

def conditcondit(operater, args):
	options = {
		"==":eq,
		"!=":neq,
		"<=":leseq,
		">=":greeq,
		">":gre,
		"<":les
	}
	return options[operater](args)
def condit(args):
	b = False
	
	ags = []
	if(args[0][0] in vars):
		ags.append(vars[args[0][0]])
	else:
		ags.append(tryInt(args[0][0]))
	if(args[0][2] in vars):
		ags.append(vars[args[0][2]])
	else:
		ags.append(tryInt(args[0][2]))
	#print(ags[0] + args[0][1]+ags[1])
	b = conditcondit(args[0][1], ags)
	if(b):
		runline(lex(args[1], args[1].split()))
def vset(args):
	try:
		ver = int(args[-1])
	except:
		ver = args[-1]
	if("=" in args and not(args[0] in vars.keys())):
		vars[args[0]] = ver
	elif("+=" in args):
		vars[args[0]] += ver
	elif("-=" in args):
		vars[args[0]] -= ver
	else:
		raise CompileError(args[1]+ " Does not exist.")
def disp(args):
	print(vars[args[0]])
for x in file:
	line = x.split()
	parsed = lex(x, line)
	#print(parsed)
	#print(parsed['operand'])
	runline(parsed)
	
	