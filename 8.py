#
def isNotAdjacent(p):
	s = str(p)
	for i in range(1,6):
		if ( s[i]==s[i-1] ):
			return False
	return True

def isNotIncreasing(p):
	s = str(p)
	for i in range(1,6):
		if ( int(s[i]) < int( s[i-1] ) ):
			return True
	return False

def isContains2xGroup(p):
	s = str(p)
	t = [s]
	more = True
	while more:
		more = False
		s = t[-1]
		for i in range(1, len(s)):
			if s[0]!=s[i]:
				t[-1] = s[0:i]
				t.append( s[i:100] )
				print t
				more = True
				break
	for i in t:
		if len(i)==2:
			
			return True
	return False
	
c = 0
for p in range(183564, 657474):
	if isNotAdjacent(p):
		continue
	if isNotIncreasing(p):
		continue
	if not isContains2xGroup(p):
		continue
	c = c +1
	
print c