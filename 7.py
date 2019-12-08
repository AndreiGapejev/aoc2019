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
	
c = 0
for p in range(183564, 657474):
	if isNotAdjacent(p):
		continue
	if isNotIncreasing(p):
		continue
	c = c +1
	
print c