from inp6 import inp

inp = inp()

def calc_orbits(start, path):
	r = 0
	for a in inp:
		if a[0]==start:
			# direct orbit
			r = r + 1
			# indirect orbits
			r = r + len(path)
			r = r + calc_orbits(a[1], path+[start])
			
	return r
	
	
print calc_orbits("COM", [])