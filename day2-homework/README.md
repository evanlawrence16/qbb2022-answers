 # QBB2022 - Day 2 - Homework Excercises Submission


Number 1

```
#!/usr/bin/env python3

#import libraries
import sys

def parse_vcf(fname):
	#empty list that will contain our output
	vcf = []
	#dictionary containing the id and description of info from info header
	info_description = {}
	#dictionary containing the id and type of info from info header
	info_type = {} 
	#dictionary containing the id and description of the information from the format header
	format_description = {}
	type_map = {
		"Float": float,
		"Integer": int,
		"String": str
		}
	#number of lines considered malformed (they don't pass our parsing conditions)
	malformed = 0

	#try and open the file
	try:
		fs = open(fname)
	#otherwise raise error that file does not exist
	except:
		raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr)

	#loops through lines in the file to parse them. Also keeps track of line #
	for h, line in enumerate(fs):

	#what to do if the line is part of the header
		if line.startswith("#"):
			try:
	#What to do with the format line in the header
				if line.startswith("##FORMAT"):
				#get rid of the symbols like > surrounding the format data and add the data to a variable 'fields'
					fields = line.split("=<")[1].rstrip(">\r\n") + ","
					i = 0
					start = 0
					in_string = False

					#step through format data and extract id and description into dictionaries
					while i < len(fields):
						#delimit the areas of the data you are breaking up- before each comma and after 1 equal sign
						if fields[i] == "," and not in_string:
							if fields[start:i].count("=") == 1:
						#split by the equal sign. Before the = becomes the name and after the = becomes value
								name, value = fields[start:i].split('=')
						#assign the values to specific variable depending on what the name is.
								if name == "ID":
									ID = value
								elif name == "Description":
									desc = value
						#steps start one index forward
							start = i + 1

						#changes the True/False value of in_string at quotation marks
						elif fields[i] == '"':
							in_string = not in_string
						#steps i one index forward
						i += 1
					#adds a dictionary where the id cooresponds to the description
					format_description[ID] = desc.strip('"')

			#what to do with the info line of the header
				elif line.startswith("##INFO"):
					#get rid of the symbols like > surrounding the info data and add the data to a variable 'fields'
					fields = line.split("=<")[1].rstrip(">\r\n") + ","
					i = 0
					start = 0
					in_string = False
					#step through format data and extract id, description, and type into dictionaries
					while i < len(fields):
						if fields[i] == "," and not in_string:
							if fields[start:i].count("=") == 1:
								name, value = fields[start:i].split('=')
								if name == "ID":
									ID = value
								elif name == "Description":
									desc = value
								elif name == "Type":
									Type = value
							start = i + 1
						elif fields[i] == '"':
							in_string = not in_string
						i += 1
					#add our extracted data to dictionaries
					info_description[ID] = desc.strip('"')
					info_type[ID] = Type

			#what to do with the column names of the file	
				elif line.startswith('#CHROM'):
					#get rid of #, spaces, and split each line into a list by tab
					fields = line.lstrip("#").rstrip().split("\t")
					#add the lists to fields 
					vcf.append(fields)

			#if this isn't possible then the column names might be formatted weirdly
			except:
				raise RuntimeError("Malformed header")

		#what to do with lines that do not start with # - the body of the file
		else:
			try:
				#try and split the line into a list by tab
				fields = line.rstrip().split("\t")
				#convert field 1 to an integer
				fields[1] = int(fields[1])

				#if field five is not a period than make it a float
				if fields[5] != ".":
					fields[5] = float(fields[5])

				#creates a dictionary info
				info = {}

				#split field 7 into entries by ;
				for entry in fields[7].split(";"):
					#split each enty by =
					temp = entry.split("=")

					#there can be entries that are either present or absent and don't = anything - so allow them to be none in the dict
					if len(temp) == 1:
						info[temp[0]] = None

					#otherwise set the dictionary where one side is the name and the other side is the value
					else:
						name, value = temp
						Type = info_type[name]
						info[name] = type_map[Type](value)
				fields[7] = info

				#if there is an eighth field then parse it
				if len(fields) > 8:
					#split the field by :
					fields[8] = fields[8].split(":")
					#if there are multiple entries in this list then split field 8 up. otherwise field 8 =the first entry
					if len(fields[8]) > 1:
						for i in range(9, len(fields)):
							fields[i] = fields[i].split(':')
					else:
						fields[8] = fields[8][0]

				#add all fields to the vcf list
				vcf.append(fields)

			#if any issues are encountered the row may be malformed. add this to our malformed tally
			except:
				malformed += 1
	vcf[0][7] = info_description
	if len(vcf[0]) > 8:
		vcf[0][8] = format_description

	#if there are malformed rows print how many there are
	if malformed > 0:
		print(f"There were {malformed} malformed entries", file=sys.stderr)
	#return the parsed data
	return vcf

#the code starts running here
if __name__ == "__main__":
	#input file is passed in terminal
	fname = sys.argv[1]
	#calling the function on input file
	vcf = parse_vcf(fname)
	#prints the first ten lines of output from the vcf parser
	for i in range(10):
		print(vcf[i])
		
```






SECOND PROBLEM

```
#!/usr/bin/env python3

#import libraries/functions
import sys
from vcf_parser_4 import parse_vcf






#the code starts running here
if __name__ == "__main__":
	#paths to each of the input files
	dbsnp="/Users/cmdb/qbb2022-answers/day2-homework/dbSNP_snippet.vcf"
	random="/Users/cmdb/qbb2022-answers/day2-homework/random_snippet.vcf"



#getting a dictionary of snps
	#parses the snp file
	vcf=parse_vcf(dbsnp)

	#lists to hold locations and ids
	lis1=[]
	lis2=[]

	#append location and ids to lists
	for i in range(len(vcf)):
		lis1.append(vcf[i][1])
		lis2.append(vcf[i][2])

	#zip the lists into a dictionary
	snpidsetc=dict(zip(lis1,lis2))


#replacing ids in the random snippit file
#opens an output file
	newfile=open("/Users/cmdb/qbb2022-answers/day2-homework/correct.vcf",'a+')

	#reads in the random file line by line
	f=open(random,'r')
	randomllines=f.readlines()
	f.close()

	#for each line in the random file 
	unlabeled=0
	for i in randomllines:
		#we either split by tab, or dump it to the output file
		try:
			list0=i.split("\t")
			#print(list0)
		except:
			line=i
			continue
		#for each line that was split by tab we try and find the position in our dictionary
		#if we do find it we replace the blank id with the new id and write that to the output
		#otherwise we just write the original line to the output and count the entry as unlabelled
		for key in snpidsetc.keys():
			if "\t"+str(key)+"\t" in i:
				list0[2]=snpidsetc[key]
				#print(list0)
				line="\t".join(list0)
				#print(line)
			else:
				line="\t".join(list0)
				unlabeled=unlabeled+1
		#print(line)
		newfile.write(line)


	#close the output file
	newfile.close()
	#print the number of entries without ids
	print(unlabeled)

```

OUTPUT=
 