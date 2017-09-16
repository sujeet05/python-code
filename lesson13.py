from sys import argv
script,filename= argv
#open the file 
txt = open(filename,'w')
print "Demonstrate the writing into file %s filename" %filename 
#read the input from user to write into the file
line1 = raw_input("give the input first line")
line2 = raw_input("give the input Second line")
line3 = raw_input("give the input Third line")
#writing into the file 
txt.write(line1)
txt.write("\n")
txt.write(line2)
txt.write("\n")
txt.write(line3)
txt.write("\n")
#closing the file 
txt.close();

#open the file to read the content .. 

open_again=open(filename)
print "Content of the files ...."
print open_again.read()
txt.close()

#demonstrate truncating the file 

#open_again = open(filename,'w')
#opening the file again in write mode .. If you go to see the content of physical file it will be showing nothing
#multiple line comment use ''' '''

'''
print "Are you sure to truncate the file %s" %filename 
print "If you don't want that, hit CTRL- C (^C)."
print "If you do want that, hit RETURN." 
raw_input("?")
print " Truncating the file GoodBye"
open_again.truncate()
open_again.close()
''''