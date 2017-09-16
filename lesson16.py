from sys import argv
script ,filefrom ,fileto =argv


infile =  open(filefrom,'r')
outfile = open(fileto,'w')
outfile.write(infile.read())

#close both the file 
infile.close()
outfile.close()
