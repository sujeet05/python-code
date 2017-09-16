from sys import argv

script , filename = argv

def printfile(f):
	print f.read()
def printfileline(lineno,f):
	print lineno ,f.readline(),
def rewind(f):
	f.seek(0)

currentfile = open(filename)
printfile(currentfile)
rewind(currentfile)
lineno =1
printfileline(lineno,currentfile)
printfileline(lineno+1,currentfile)
printfileline(lineno+2,currentfile)