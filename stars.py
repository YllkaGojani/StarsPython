x=[1,5,3,6,2]
y=[1,"Yllka",3,"Gojani",5]	


# def draw_stars(x):
# 	for i in range(0,len(x)):
# 		print '*'*x[i]

def draw_stars(x):
	for i in range(0,len(x)):
		if isinstance(x[i], str):
			string = x[i][0].lower()+''
			print string*len(x[i])
		else:
			print '*'*x[i]		

draw_stars(x)
draw_stars(y)	