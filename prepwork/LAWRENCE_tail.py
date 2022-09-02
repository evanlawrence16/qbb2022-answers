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


