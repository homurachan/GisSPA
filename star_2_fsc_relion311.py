#!/usr/bin/env python

import math, os, sys, random
try:
	from optparse import OptionParser
except:
	from optik import OptionParser

def main():
	(starfile, fscfile) =  parse_command_line()
	g = open(starfile, "r")
	r=open(fscfile,"w")
	star_line=g.readlines()

	for i in range(0,len(star_line)):
		if(star_line[i].split()):
			if str(star_line[i].split()[0])=="_rlnResolution":
				res_index=int(star_line[i].split('#')[1])
			if str(star_line[i].split()[0])=="_rlnFourierShellCorrelationCorrected":
				nus=int(star_line[i].split('#')[1])
				n=i
#	print n
#	print len(star_line)
	for i in range (n+5,len(star_line)):
	#	print star_line[i]
		if len(star_line[i].split())==0:
			break
		res=star_line[i].split()[res_index-1]
		fsc=star_line[i].split()[nus-1]
	#	print res
	#	print fsc
		r.write(str(res)+"\t"+str(fsc)+"\n")

	g.close()
	r.close()

	
def parse_command_line():
	usage="%prog <starfile> <fscfile>"
	parser = OptionParser(usage=usage, version="%1")
	
	if len(sys.argv)<3: 
		print "<starfile> <fscfile>"
		sys.exit(-1)
	
	(options, args)=parser.parse_args()
	
	starfile = args[0]
	fscfile = args[1]
	return (starfile, fscfile)

if __name__== "__main__":
	main()


			
