inp = [[]]
signals = []
pointer = []
cycle = -1
inp[0] = [3,8,1001,8,10,8,105,1,0,0,21,30,39,64,81,102,183,264,345,426,99999,3,9,1001,9,2,9,4,9,99,3,9,1002,9,4,9,4,9,99,3,9,1002,9,5,9,101,2,9,9,102,3,9,9,1001,9,2,9,1002,9,2,9,4,9,99,3,9,1002,9,3,9,1001,9,5,9,1002,9,3,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,4,9,9,1001,9,5,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,99]

def reset():
	global inp, signals, pointer, cycle
	global halt
	inp = inp[0:1]
	signals = []
	pointer = []
	cycle = -1
	pointer.append(0)
	for i in range(1, 5):
		inp.append(inp[0][:])
		pointer.append(0)
	halt = False
		

halt = False
debug = True

def get_param(computer, mode, value):
	if debug:
		print "get_param", locals()
	if mode=="1":
		return value
	if mode=="0":
		return inp[computer][value]
	return "ERROR"
	
def get_param_by_id(computer, cur, id):
	s = "%05d" % (inp[computer][cur])
	parameter_modes = s[:3]
	if id==1:
		return get_param(computer, parameter_modes[2], inp[computer][cur+1]) 
	if id==2:
		return get_param(computer, parameter_modes[1], inp[computer][cur+2]) 
	return ERROR_get_param_by_id
	
def set_param(computer, mode, param, value):
	if debug:
		print "set_param", locals()
	if mode=="0":
		inp[computer][param] = value
	if mode=="1":
		print ERROR
	return 

def runProg(computer):
	global halt
	halt = False
	
	cur = pointer[computer]
	output = []
	while inp[computer][cur] != 99:
		s = "%05d" % (inp[computer][cur])
		instruction = s[-2:]
		parameter_modes = s[:3]
		
		if debug:
			print cur, instruction, parameter_modes
		delta = 0
		if instruction == "01":
			p1 = get_param_by_id(computer, cur, 1)
			p2 = get_param_by_id(computer, cur, 2)
			set_param(computer, parameter_modes[0], inp[computer][cur+3], p1+p2 )
			delta = 4
		if instruction == "02":
			p1 = get_param_by_id(computer, cur, 1)
			p2 = get_param_by_id(computer, cur, 2)
			set_param(computer, parameter_modes[0], inp[computer][cur+3], p1*p2 )
			delta = 4
		if instruction == "03":
			if len( signals[computer][0]) ==0:
				pointer[computer] = cur
				return
			
			p1 = get_param(computer, "1", inp[computer][cur+1]) 
			p2 = signals[computer][0][0]
			signals[computer][0] = signals[computer][0][1:]
			if debug:
				print "Input=", p2 , signals[computer][0]
			dump_computers()
			set_param(computer, "0", p1, p2 )
			dump_computers()
			delta = 2
		if instruction == "04":
			p1 = get_param(computer, "0", inp[computer][cur+1]) 
			if debug:
				print "Output=", p1
			signals[(computer+1)%5][0].append(p1)
			if computer==4:
				signals[(computer)%5][1].append(p1)
			delta = 2
			
		# Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
		if instruction == "05":
			p1 = get_param_by_id(computer, cur, 1)
			p2 = get_param_by_id(computer, cur, 2)
			if p1>0:
				delta = p2-cur
			else:
				delta = 3
		# Opcode 6 is jump-if-false: if the first parameter is zero, it sets the instruction pointer to the value from the second parameter. Otherwise, it does nothing.
		if instruction == "06":
			p1 = get_param_by_id(computer, cur, 1)
			p2 = get_param_by_id(computer, cur, 2)
			if p1==0:
				delta = p2-cur
			else:
				delta = 3
		# Opcode 7 is less than: if the first parameter is less than the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0
		if instruction == "07":
			p1 = get_param_by_id(computer, cur, 1)
			p2 = get_param_by_id(computer, cur, 2)
			if p1<p2:
				set_param(computer, "0", inp[computer][cur+3], 1 )
			else:
				set_param(computer, "0", inp[computer][cur+3], 0 )
			delta = 4
			
		# Opcode 8 is equals: if the first parameter is equal to the second parameter, it stores 1 in the position given by the third parameter. Otherwise, it stores 0
		if instruction == "08":
			p1 = get_param_by_id(computer, cur, 1)
			p2 = get_param_by_id(computer, cur, 2)
			if p1==p2:
				set_param(computer, "0", inp[computer][cur+3], 1 )
			else:
				set_param(computer, "0", inp[computer][cur+3], 0 )
			delta = 4
		
			
		if delta == 0:
			print ERROR_delta_0
			break
			
		cur = cur + delta
		pointer[computer] = cur
	if computer==4:
		halt = True
	
	return signals[0][0]

	

def dump_computers():
	
	print "\t\t\t\t\t\t\t\t\tComputers = \n"
	for a in inp:
		print a
def findValue(seq):
	global inp, signals, pointer, cycle
	global halt
	reset()
	signals.append( [ [seq[0], 0] , [] ] )
	for i in range(1, 5):
		signals.append( [ [seq[i]] , [] ])
	
	
		
	while halt==False:	
		cycle = cycle + 1
		print "\t\t\t\t\t\t\t\t\tComputer = " , cycle%5, "Cycle=", cycle, "io=", signals
		dump_computers()
		
		runProg(cycle%5)
		#if cycle==10:
		#	break
		print cycle
		if halt==True:
			break
	print "\t\t\t\t\t\t\t\t\tComputer = " , cycle%5, "Cycle=", cycle, "io=", signals
	return [ seq, max( signals[4][1] + [0] ) ]
	

	
def test1():
	# Expect Output= 139629729 139629729
	global inp
	inp[0] = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
	reset()
	debug = True
	print findValue([9,8,7,6,5])
	
def test2():
	# Expect Output= 18216 18216
	global inp
	inp[0] = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
	reset()
	debug = True
	print findValue([9,7,8,5,6])
	
def test52():
	# Expect Output= 513116
	debug = True
	pointer.append(0)
	signals.append( [ [5] , [] ] )
		
	inp[0] = [3,225,1,225,6,6,1100,1,238,225,104,0,1101,81,30,225,1102,9,63,225,1001,92,45,224,101,-83,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1102,41,38,225,1002,165,73,224,101,-2920,224,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,1101,18,14,224,1001,224,-32,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,1101,67,38,225,1102,54,62,224,1001,224,-3348,224,4,224,1002,223,8,223,1001,224,1,224,1,224,223,223,1,161,169,224,101,-62,224,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,2,14,18,224,1001,224,-1890,224,4,224,1002,223,8,223,101,3,224,224,1,223,224,223,1101,20,25,225,1102,40,11,225,1102,42,58,225,101,76,217,224,101,-153,224,224,4,224,102,8,223,223,1001,224,5,224,1,224,223,223,102,11,43,224,1001,224,-451,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,1102,77,23,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,677,224,1002,223,2,223,1006,224,329,1001,223,1,223,7,226,226,224,102,2,223,223,1006,224,344,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,359,101,1,223,223,1107,226,677,224,1002,223,2,223,1005,224,374,101,1,223,223,1008,677,226,224,1002,223,2,223,1005,224,389,101,1,223,223,1007,677,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,419,1001,223,1,223,108,677,226,224,102,2,223,223,1006,224,434,1001,223,1,223,7,226,677,224,102,2,223,223,1005,224,449,1001,223,1,223,107,226,226,224,102,2,223,223,1006,224,464,101,1,223,223,107,677,226,224,102,2,223,223,1006,224,479,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,494,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,509,101,1,223,223,7,677,226,224,1002,223,2,223,1006,224,524,1001,223,1,223,1007,226,226,224,102,2,223,223,1006,224,539,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,554,101,1,223,223,1008,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,584,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,599,1001,223,1,223,1108,677,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,1107,677,677,224,1002,223,2,223,1005,224,629,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,644,101,1,223,223,8,226,226,224,1002,223,2,223,1005,224,659,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,674,101,1,223,223,4,223,99,226]
	print runProg(0)

def main():
	#Wrong - 947378
	import itertools 
	l = [5,6,7,8,9]
	perm = itertools.permutations(l) 
	mx = [[], 0]
	
	for i in list(perm): 
		halt = False
		reset()
		t = findValue(i)
		if t[1]> mx[1]:
			mx = t
	print mx

debug = False
#test1()
#test2()
#test52()
main()
