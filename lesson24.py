i=0
elements =[]
while i < 6 :
	print " inserting the element in list %d" %i
	elements.append(i)
	i=i+1
	print " Before going for next iteration value of i %d" %i
print "print the list"
for num in elements:
	print "List elements :%d" %num