from sys import argv

script,user_name = argv
prompt = ">"
print "HI %s i am using %s " %(user_name,script)
print " i would like to ask you few Questions"
print " Do you like me %s"  %user_name
likes = raw_input(prompt)

print " where do you live %s " %user_name
live = raw_input (prompt)
print " what kind of computer do you have "
computer = raw_input(prompt)
print """
 Alright, so you said %r about liking me.
 You live in %r. Not sure where that is.
 And you have a %r computer. Nice.
 """ % (likes, live, computer)