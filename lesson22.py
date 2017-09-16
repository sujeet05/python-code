print "Enter the option to chose the carrier path"
print " Choose option from below:"
print "postgraduate"
print "graduate"
print "intermediate"
print "matriculation"
value = raw_input(">")
if value=="postgraduate":
	print "Enter options from below available options "
	print "Computer science & mathematics"
	print "Commerce"
	print "Others"
	stream =raw_input("stream:")
	if stream =="Computer science & mathematics ":
		print " Can seek in IT induustry for hefty salary"
	elif stream == "Commerce":
		print " can look into Charted Accountant and cost Accountancy"
	else:
		print " can apply for general services like PO and Assistant Grade"
elif value=="graduate":
	print " Apply for post graduation "
elif value=="intermediate":
	print " Enter 1 for science 2 for Arts 3 for Commerce "
	option =int(raw_input("option:"))
	if (option==1):
		print "can prepare for Engineering and medical"
	elif (option==2):
		print "can focus on general and civil services"
	else:
		print "focus on CA services"
else:
	print "Too early to comment"

