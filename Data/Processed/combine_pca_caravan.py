#read tictgts2000.txt
target_array = []
with open('ticdata2000.txt') as tgts:
	tgts 
	for target in tgts:
		if 'CARAVAN' not in target:
			x = target.split('\t')[-1]
			target_array.append(x)
		
#print len(target_array)
#print target_array

#read pca_data.csv
with open('pca_data.csv', 'r') as pca:
	i = 0
	with open('pca_data_target.csv', 'w') as d:
		for l in pca:
			if 'pc' not in l:
				x = l.rstrip() + ":" + target_array[i]
				d.write(x)
				i += 1
