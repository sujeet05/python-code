ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Wait there's not 10 things in that list, let's fix that."
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff)!=10:
	next_one =more_stuff.pop()
	stuff.append(next_one)
	print "there is %d items in stuff" % len(stuff)
print "Lists is", stuff
print "some More experiements with lists"

print stuff[1]
print stuff[-1]
print stuff.pop()
print '#'.join(stuff) # what? cool!
print stuff[3:7]
print '#'.join(stuff[3:5])

