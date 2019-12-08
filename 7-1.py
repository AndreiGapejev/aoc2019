inp = [3,8,1001,8,10,8,105,1,0,0,21,30,39,64,81,102,183,264,345,426,99999,3,9,1001,9,2,9,4,9,99,3,9,1002,9,4,9,4,9,99,3,9,1002,9,5,9,101,2,9,9,102,3,9,9,1001,9,2,9,1002,9,2,9,4,9,99,3,9,1002,9,3,9,1001,9,5,9,1002,9,3,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,4,9,9,1001,9,5,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,99]




def get_param(mode, value):
	debug = False
	if debug:
		print "get_param", locals()
	if mode=="1":
		return value
	if mode=="0":
		return inp[value]
	return "ERROR"
	
def get_param_by_id(cur, id):
	s = "%05d" % (inp[cur])
	parameter_modes = s[:3]
	if id==1:
		return get_param(parameter_modes[2], inp[cur+1]) 
	if id==2:
		return get_param(parameter_modes[1], inp[cur+2]) 
	return ERROR_get_param_by_id
	
def set_param(mode, param, value):
	debug = False
	if debug:
		print "set_param", locals()
	if mode=="0":
		inp[param] = value
	if mode=="1":
		print ERROR
	return 

def runProg(prog_input):
	debug = False
	next_input = 0
	cur = 0
	while inp[cur] != 99:
		s = "%05d" % (inp[cur])
		instruction = s[-2:]
		parameter_modes = s[:3]
		
		if debug:
			print cur, instruction, parameter_modes
		delta = 0
		if instruction == "01":
			p1 = get_param_by_id(cur, 1)
			p2 = get_param_by_id(cur, 2)
			set_param(parameter_modes[0], inp[cur+3], p1+p2 )
			delta = 4
		if instruction == "02":
			p1 = get_param_by_id(cur, 1)
			p2 = get_param_by_id(cur, 2)
			set_param(parameter_modes[0], inp[cur+3], p1*p2 )
			delta = 4
		if instruction == "03":
			p1 = get_param("1", inp[cur+1]) 
			p2 = prog_input[next_input]
			next_input = next_input + 1
			if debug:
				print "Input=", p2
			set_param("0", p1, p2 )
			delta = 2
		if instruction == "04":
			p1 = get_param("0", inp[cur+1]) 
			if debug:
				print "Output=", p1
			return p1
			delta = 2
		# Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
		if instruction == "05":
			p1 = get_param_by_id(cur, 1)
			p2 = get_param_by_id(cur, 2)
			if p1>0:
				delta = p2-cur
			else:
				delta = 3
		# Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
		if instruction == "06":
			p1 = get_param_by_id(cur, 1)
			p2 = get_param_by_id(cur, 2)
			if p1==0:
				delta = p2-cur
			else:
				delta = 3
		# Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0
		if instruction == "07":
			p1 = get_param_by_id(cur, 1)
			p2 = get_param_by_id(cur, 2)
			if p1<p2:
				set_param("0", inp[cur+3], 1 )
			else:
				set_param("0", inp[cur+3], 0 )
			delta = 4
			
		# Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0
		if instruction == "08":
			p1 = get_param_by_id(cur, 1)
			p2 = get_param_by_id(cur, 2)
			if p1==p2:
				set_param("0", inp[cur+3], 1 )
			else:
				set_param("0", inp[cur+3], 0 )
			delta = 4
		
			
		if delta == 0:
			print ERROR_delta_0
			break
			
		cur = cur + delta

def work():
	import itertools 
	l = [0,1,2,3,4]
	perm = itertools.permutations(l) 

		
	mx = [[], 0]
	for i in list(perm): 
		next_prog_inp = 0
		for j in i:
			next_prog_inp = runProg([j, next_prog_inp])
		if next_prog_inp> mx[1]:
			mx = [l, next_prog_inp]
	print mx
	
def test1():
	inp = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
	work()
	
test1()