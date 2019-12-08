from inp6 import inp

inp = inp()
found = []

def way(path, to):
	if (path[-1]==to):
		print "%s %d" % (path, len(path))
		return path
	for a in inp:
		if a[0]==path[-1]:
			if a[1] in path:
				continue
			w = way(path + [a[1]], to)
			if w!=[]:
				return w
	return []
	
w1=way(['COM'], 'SAN')
w2=way(['COM'], 'YOU')

print "%s %s" % (w1, w2)


while w1[0]==w2[0]:
	w1 = w1[1:]
	w2 = w2[1:]

print "%s %s" % (w1, w2)
print len(w1) + len(w2) - 2