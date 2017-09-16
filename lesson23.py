the_count =[1,2,3,4,5]
fruits=['apple','Orange','Guava','Watermelon','Grapes']
change=[1,'pennies',2,'dimmes',3,'quarters']

for number in the_count:
	print "this is the count %d" %number
for fruit in fruits:
	print "A fruit of type %s" %fruit
for i in change :
	print "i got %r" %i
elements =[]
for i in range(0,6):
	"Adding %d the the list" %i
	elements.append(i)
for i in elements:
	print "Elements was %d" %i