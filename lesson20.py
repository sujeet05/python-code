def add(x,y):
	return x+y
def substract(x,y):
 	return x-y
def multiply(x,y):
 	return x*y
def division(x,y):
 	return x/y
def return_morethanone(x,y):
	return x+y,x-y 	
addition = add(20,5)
print addition
print "addition of 20 and 5 is %r " %add(20,5)
print "substraction of 20 and 5 is %r " %substract(20,5) 
print "multiply of 20 and 5 is %r " %multiply(20,5) 
print "division of 20 and 5 is %r " %division(20,5) 
print "sum and substraction of 20,10 %r %r" %return_morethanone(20,10)
