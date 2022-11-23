#!/bin/python3.8
import sys

file1 = open(sys.argv[1], 'r')
lines = file1.readlines()[1:]

extra = int(sys.argv[2])

for line in lines:
	file = line.split("\t")
	exonCount = int(file[8])
	cdsStart = int(file[6])
	cdsEnd = int(file[7])
	start = file[9].split(",")
	end = file[10].split(",")
	i = 0
	if	file[3] == "-":
		while exonCount > 0:
			exonstart = int(start[i])
			exonend = int(end[i])
			exon = exonCount
			exonCount = exonCount - 1
			i = i + 1
			if (exonstart < cdsStart) and (exonend > cdsStart):
				if exonend>cdsEnd:
					print(file[2],cdsStart-extra,cdsEnd+extra,file[12]+"_"+file[1]+"_["+str(exon)+"]", sep='\t', end="\n")
				else:
					print(file[2],cdsStart-extra,exonend+extra,file[12]+"_"+file[1]+"_["+str(exon)+"]", sep='\t', end="\n")
			elif exonstart > cdsStart:
				if (exonend > cdsEnd) and (exonstart < cdsEnd):
					print(file[2],exonstart-extra,cdsEnd+extra,file[12]+"_"+file[1]+"_["+str(exon)+"]", sep='\t', end="\n")
				elif (exonstart < cdsEnd) and (exonend < cdsEnd):
					print(file[2],exonstart-extra,exonend+extra,file[12]+"_"+file[1]+"_["+str(exon)+"]", sep='\t', end="\n")
	if file[3] == "+":
		while i < exonCount:
			exonstart = int(start[i])
			exonend = int(end[i])
			i = i + 1
			if (exonstart < cdsStart) and (exonend > cdsStart):
				if	exonend > cdsEnd:
					print(file[2],cdsStart-extra,cdsEnd+extra,file[12]+"_"+file[1]+"_["+str(i)+"]", sep='\t', end="\n")
				else:
					print(file[2],cdsStart-extra,exonend+extra,file[12]+"_"+file[1]+"_["+str(i)+"]", sep='\t', end="\n")
			elif exonstart > cdsStart:
				if (exonend > cdsEnd) and (exonstart < cdsEnd):
					print(file[2],exonstart-extra,cdsEnd+extra,file[12]+"_"+file[1]+"_["+str(i)+"]", sep='\t', end="\n")
				elif (exonstart<cdsEnd) and (exonend < cdsEnd):
					print(file[2],exonstart-extra,exonend+extra,file[12]+"_"+file[1]+"_["+str(i)+"]", sep='\t', end="\n")
