x = ""
with open('names', "r") as f:
	i = 0
	for l in f:
		if l != '\n':
			x += "\t"
			x += l.split(" ")[1]
			i+=1
			print i
print x
