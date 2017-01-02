from time import *

t1 = time()
for i in range(2000000):
	pass
t2= time()
print "%r seconds" % (t2-t1)
