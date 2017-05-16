val = input("plesae input the temp:")
if val[-1] in ['C','c']:
	f =1.8*eval(val[0:-1])+32
	print("the temp is %.2f" %f)
elif val[-1] in ['F','f']:
	c=(float(val[0:-1])-32)/1.8
	print("the temp is %.2f"%c)
else:
	print("error")
