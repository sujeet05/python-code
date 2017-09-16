def print_1(*args):
	arg1,arg2 = args
	print " First Function is called with arg* argument"
	print "arg1 %s and arg2 is %s" %(arg1,arg2)
def print_2(arg1,arg2):
	print " Second Function is called with two argument "
	print "arg1 %s and arg2 is %s" %(arg1,arg2)
def print_3(arg1):
	print " Third Function is called with one argument "
	print " arg1 is %s  " %(arg1)
def print_4():
	print " Fourth Functino is called without any argument"
	print " Fuunction called with out argument"

# Function defination is over now lets call each function 
print_4()
print_3("sujeet singh")
print_2("sujeet","kumar")
print_1("sujeet" ,"singh")