def lex(line, split):
	ret = {}
	ne = ""
	funcsplit = line.replace(";", " ").replace("(", " ").replace(")", " ").split()
	#print(funcsplit)
	nesplit = line.replace(";", " ").replace("(", " ").replace(")", " ").split()
	nesplit.pop(0)
	#print(nesplit)
	if("v" in split):
		ret["operand"] = "vset"
		ret["args"] = nesplit
		#print(ret["args"])
	if("print" in funcsplit):
		ret["operand"] = "print"
		#print(funcsplit)
		funcsplit.pop(0)
		ret["args"] = funcsplit
	if("if" in funcsplit):
		ret['operand'] = "if"
		#parsedbool = False
		boolstatement = (line[line.find("(")+1:line.find(")")]).split()
		#print(boolstatement)
		
		ret['args'] = [boolstatement, line[line.find("{")+1:line.find("}")]]
	

	return ret
	# basically needs to return a dict with the following syntax:
	#{op:"", args:[arg1, arg2, ...]}