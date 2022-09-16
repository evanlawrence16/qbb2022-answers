#!/usr/bin/env python3
import sys
from fasta import readFASTA
import numpy as np
import math

#these lists will hold the final alignments
align1=[]
align2=[]

#function to get the score of a specific alignment between 2 bps
def scoregetter(sequence1, sequence2, score):
    rowa="a"
    columa="a"
    #gets the row of the first bp
    for row in range(score.shape[0]):
        if sequence1==score[row,0]:
            rowa=row
    #gets the column for the second bp
    for col in range(score.shape[1]):
        if sequence2==score[0,col]:
            columa=col
    #gets the score at the row/column identified
    scorex=int(score[rowa,columa])
    return scorex

#opening my outfile and reading scoring matrix
outfile=open(sys.argv[4],'w')
scoringp=open(sys.argv[2],'r')
scoring=scoringp.read()
scoringp.close()
gap_penalty=int(sys.argv[3])

#getting and processing input sequences
input_sequences = readFASTA(open(sys.argv[1]))

#holding the two input sequences
seq1_id, sequence1 = input_sequences[1]
seq2_id, sequence2 = input_sequences[0]

#sequence1='TCTGCTGG'
#sequence2='CGGCTGGT'
#sequence1="TAGTAGTAGT"
#sequence2='TAGGTAGTAG'


#formatting scores into a numpy array with the proper shape
scores=scoring.split()
score=np.array(scores)
score=np.insert(score, 0, "blank")
score=score.reshape(int(math.sqrt(len(score))),int(math.sqrt(len(score))))

#=====================#
# Initialize F-matrix #
#=====================#

# The first thing we need to do is create an empty F-matrix.
# The number of rows should be equal to the length of
# sequence1 plus one (to allow for leading gaps). Similarly,
# the number of columns should be equal to the length of
# sequence2 plus one.

F_matrix = np.zeros((len(sequence1)+1, len(sequence2)+1))
Traceback = np.zeros((len(sequence1)+1, len(sequence2)+1),str)

# Now we need to fill in the values in the first row and
# first column, based on the gap penalty. Let's fill in the
# first column.
for i in range(len(sequence1)+1):
    F_matrix[i,0] = i*gap_penalty
    Traceback[i,0] = 1

# Now fill in the first row
for j in range(len(sequence2)+1):
    F_matrix[0,j] = j*gap_penalty
    Traceback[0,j] = 3

#=======================#
# Populate the F-matrix #
#=======================#
# Now that we've filled in the first row and column, we need
# to go row-by-row, and within each row go column-by-column,
# calculating the scores for the three possible alignments
# and storing the maximum score

for i in range(1, len(sequence1)+1): # loop through rows
    for j in range(1, len(sequence2)+1): # loop through columns
        if sequence1[i-1] == sequence2[j-1]: # if sequence1 and sequence2 match at positions i and j, respectively...
        #send the alignment to the scoregetter function and return score
            d = F_matrix[i-1, j-1] + scoregetter(sequence1[i-1], sequence2[j-1], score )
        else: # if sequence1 and sequence2 don't match at those positions...
            d = F_matrix[i-1, j-1] + scoregetter(sequence1[i-1], sequence2[j-1], score )
        #otherwise add the gap penalty
        h = F_matrix[i,j-1] + gap_penalty
        v = F_matrix[i-1,j] + gap_penalty

        #make the traceback matrix.
        #1 is a gap in sequence 2
        #3 is a gap in sequence 1
        #2 is a bp-bp alignment
        #5 is a tie
        if d>v and d>h:
            Traceback[i,j]=2
        elif h>v and h>d:
            Traceback[i,j]=3
        elif v>h and v>d:
            Traceback[i,j]=1
        else:
            Traceback[i,j]=5

        #handling ties
        if int(Traceback[i,j])==5:
            if d==v or d==h:
                Traceback[i,j]=2
            elif v==h:
                Traceback[i,j]=3

    #getting the max to populate the matrix
        F_matrix[i,j] = max(d,h,v)

#sequence 2 is row
#sequence 1 is column

#setting start coordinates at bottom left corner
a=F_matrix.shape[0]-1
b=F_matrix.shape[1]-1

#get the alignment score
alignment_score=F_matrix[a,b]

#keep track of number of gaps
seq1gaps=0
seq2gaps=0

#build the alignments until we are at the top right corner [0,0]
while a+b>0:
    #depending on what path the algorithm picked at each point
    #add a bp or gap to each alignment
    #and use the traceback matrix to find where we are headed next
    if int(Traceback[a,b])==2:
        #print(Traceback[a,b])
        align1.append(sequence1[a-1])
        align2.append(sequence2[b-1])
        a=a-1
        b=b-1
    elif int(Traceback[a,b])==3:
        #print(Traceback[a,b])
        align1.append('-')
        align2.append(sequence2[b-1])
        seq2gaps=seq2gaps+1
        a=a
        b=b-1
    elif int(Traceback[a,b])==1:
        #print(Traceback[a,b])
        align1.append(sequence1[a-1])
        align2.append("-")
        seq1gaps=seq1gaps+1
        a=a-1
        b=b

#reverse the final alignments
align1.reverse()
align2.reverse()
#format and print output
str1=''
alignment1=str1.join(align1)
alignment2=str1.join(align2)
print("sequence 1 has "+str(seq1gaps)+" gaps")
print("sequence 2 has "+str(seq2gaps)+" gaps")
print("alignment score= "+str(alignment_score))
#print(alignment1)
#print(alignment2)

#====================#
# Print the F-matrix #
#====================#
#print(F_matrix)
#print(Traceback)
outfile.write("Seq_1:"+alignment1+"\n"+"Seq_2:"+alignment2)
#np.savetxt("/Users/cmdb/qbb2022-answers/week2-homework/numpy.txt",F_matrix)
outfile.close()
