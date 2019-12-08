#
inp = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,81,30,225,1102,9,63,225,1001,92,45,224,101,-83,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1102,41,38,225,1002,165,73,224,101,-2920,224,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,1101,18,14,224,1001,224,-32,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,1101,67,38,225,1102,54,62,224,1001,224,-3348,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,1,161,169,224,101,-62,224,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,2,14,18,224,1001,224,-1890,224,4,224,1002,223,8,223,101,3,224,224,1,223,224,223,1101,20,25,225,1102,40,11,225,1102,42,58,225,101,76,217,224,101,-153,224,224,4,224,102,8,223,223,1001,224,5,224,1,224,223,223,102,11,43,224,1001,224,-451,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1102,77,23,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,677,224,1002,223,2,223,1006,224,329,1001,223,1,223,7,226,226,224,102,2,223,223,1006,224,344,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,359,101,1,223,223,1107,226,677,224,1002,223,2,223,1005,224,374,101,1,223,223,1008,677,226,224,1002,223,2,223,1005,224,389,101,1,223,223,1007,677,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,419,1001,223,1,223,108,677,226,224,102,2,223,223,1006,224,434,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,449,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,464,101,1,223,223,107,677,226,224,102,2,223,223,1006,224,479,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,494,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,509,101,1,223,223,7,677,226,224,1002,223,2,223,1006,224,524,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,539,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,554,101,1,223,223,1008,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,584,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,599,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,1107,677,677,224,1002,223,2,223,1005,224,629,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,644,101,1,223,223,8,226,226,224,1002,223,2,223,1005,224,659,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,674,101,1,223,223,4,223,99,226]

def get_param(mode, value):
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
	print "set_param", locals()
	if mode=="0":
		inp[param] = value
	if mode=="1":
		print ERROR
	return 
	
cur = 0
while inp[cur] != 99:
	s = "%05d" % (inp[cur])
	instruction = s[-2:]
	parameter_modes = s[:3]
	
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
		print "Enter input?"
		p2 = 5
		set_param("0", p1, p2 )
		delta = 2
	if instruction == "04":
		p1 = get_param("0", inp[cur+1]) 
		print "Output=", p1
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
		print "ERROR"
		break
		
	cur = cur + delta
	
	
print inp