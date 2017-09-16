#define the function with arguments 
def Calculate_interest(principle,time,roi):
	print " Given principle %r,time %r and rate of interest %r" %(principle,time,roi)
	interest = principle*time*roi/100
	print " Interest is %r" %(interest)

#define the variable which will be passed in functinon
principle= int(raw_input("principle->"))
time= int(raw_input("time->"))
roi= int(raw_input("roi->"))
#call the function pass the argument 
Calculate_interest(principle,time,roi)

print "calculate interest of 500,2,9" 
Calculate_interest(500,2,9)
Calculate_interest(principle+500,time+6,roi+5)
Calculate_interest(500+500,2+3,9+1)
