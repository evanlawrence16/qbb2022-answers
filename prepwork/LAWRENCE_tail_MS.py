import sys #import module
filename = sys.argv[1] #SET input filename
if len(sys.argv) > 2: #IF user-specified number of lines provided
  n_lines = int(sys.argv[2]) #SET the desired number of lines
else: #otherwise set lines to 10
  n_lines = 10
f = open(filename, "r")#open file
lines=f.readlines()#create list of lines
f.close()#close file
nlines=len(lines)#get number of lines in file
toprint=lines[nlines-n_lines:nlines] #get lines to print
for line in toprint: #print lines
    print(line.strip('\r\n'))

# This looks great. The code does exactly what it is supposed to. My only
# feedback is about readability. Adding blank lines to break the code into
# functional blocks makes it much easier to follow. Otherwise, your comments
# are clear and your code is clean and concise. Keep up the great work! - Mike