from sys import argv
script,filename= argv
#open the file 
txt = open(filename,'w')
print "Are you sure to truncate the file %s" %filename 
print "If you don't want that, hit CTRL- C (^C)."
print "If you do want that, hit RETURN." 
raw_input("?")
print " Truncating the file GoodBye"
#txt.truncate()
txt.close()