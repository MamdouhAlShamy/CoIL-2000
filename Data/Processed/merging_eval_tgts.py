#read tictgts2000.txt
target_array = []
with open('tictgts2000.txt') as tgts:
	for target in tgts:
		target_array.append(target)
		
#print target_array

#read ticeval2000.txt
with open('ticeval-tgts2000.txt', 'w') as f:
	i = 0
	with open('ticeval2000.txt') as eval:
		for l in eval:
			x = l.rstrip() + "\t" + target_array[i]
			f.write(x)
			i += 1
	

		
#create ticeval-tgts2000.txt
