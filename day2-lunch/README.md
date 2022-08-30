 # QBB2022 - Day 2 - Lunch Exercises Submission
1. EXTENDED BED PARSER
```
#!/usr/bin/env python3
#imports required packages
import sys

#function to parse bed file
def parse_bed(fname):
#empty list to hold our output
    bed = []
#data types of the input fields
    field_types = [str, int, int, str, str, str,int,int,str,str,str]

#open the input file or raise an error
    try:
        fs = open(fname, 'r')
    except:
        raise FileNotFoundError("That file doesn’t appear to exist")

#for each line in the file
    for i, line in enumerate(fs):
#skip lines that start with #
        if line.startswith("#"):
            continue
#format the lines as a list without spaces
        fields = line.rstrip().split()
#get the number of entries per line
        fieldN = len(fields)
            

#make sure the line has the proper number of fields or skip it
        if fieldN < 3 or fieldN==10 or fieldN==11:
            print(f"Line {i} has not enough/too many fields, requires Bed3 or greater and not Bed10 or 11", file=sys.stderr)
            continue
 
 #make sure the fields are the proper data type or raise an error       
        try:
            for j in range(min(len(field_types), len(fields))):
                fields[j] = field_types[j](fields[j])
            bed.append(fields)
        except:
            print(f"Line {i} appears malformed", file=sys.stderr)


#ensure that field 9 contains 3 items and these items are integers
        if fieldN>8:
            itemrgb=fields[8].split(",")
            if len(itemrgb)!=3:
                print(f"Line {i} itemrgb does not contain 3 items", file=sys.stderr)
            for t in itemrgb:
                try:
                    t=int(t)
                except:
                    print(f"Line {i} itemrgb contains data that are not integers", file=sys.stderr)

#make sure block sizes and block counts are equal
        if fieldN>11:
            sizes=fields[10].split(",")
            sizes.remove("")
            counts=fields[11].split(",")
            counts.remove("")
            if len(sizes)!=len(counts):
                print(f"Line {i} blockSizes and blockCounts are unequal", file=sys.stderr)




#close input file
    fs.close()
#return function output
    return(bed)


if __name__ == "__main__":
    #input file is specified through command line
    fname = sys.argv[1]
    #do the function on the input
    bed = parse_bed(fname)
    #print first two lines of output
    for i in range(2):
        print(bed[i])

```