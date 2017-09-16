from sys import argv
from os.path import exists

script ,filefrom ,fileto =argv

print"we will be reading from %s and writing it into %s" %(filefrom,fileto)
#Read the file filfrom contents into buffer
infile = open(filefrom,'r')
input = infile.read()
#get the size of the input 
print "size of the contents to be written %s bytes" %len(input)

#check does file exists to be written
print " Does the output file exist %s" %exists(fileto)
print "Ready, hit RETURN to continue, CTRL- C to abort."

outfile = open(fileto,'w')
outfile.write(input)

#close both the file 
infile.close()
outfile.close()