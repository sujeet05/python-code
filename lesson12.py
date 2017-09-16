from sys import argv
script ,filename =argv
txt =open(filename)
print " Here is your file contents %s" %filename
print txt.read() 
txt.close()
file_again = raw_input("Give the file name again...>")
content= open(file_again)
print "Reading the file again....\n"
print content.read()
content.close()
#print content.read()
#After closing the file attempting to read the content will give error 