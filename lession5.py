#x = "There are many dogs in this society %d ", 10
x = "There are %d types of people." % 10
print x
# before 10 % is mising in line no 1 . % is mandatory
binary ="binary"
dont ="dont"
#y = "those who knows %r can't say %s" (%binary,%dont)
y = "those who knows %r can't say %s" %(binary,dont)
# % should be before bracket in line no 7 
print y 
print "i said %r " %x
print "i also said %s " %y

hilarious = False 
innovative_joke = " i am doing %r "

print "it is %s to do some %r" %(hilarious,innovative_joke)
print "simply testing printing %r " %(innovative_joke)
print innovative_joke % hilarious

s= " this is the last sample"
t = " to be tested "
print s+t
print s+t+"sujeet"
print s+t+innovative_joke % hilarious