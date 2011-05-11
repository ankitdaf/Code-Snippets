import sys
text_file=open("xdupes.txt","r")
lines=text_file.readlines()
text_file.close()
text_file=open("xdupes_rm.sh","w")
my_count=len(lines)

for i in range(my_count):
	next_count = i + 1
	if next_count == my_count:
		pass				# escape hatch
	else:
		if len(lines[next_count]) > 1:		# next line is not blank, so rm this line
			out_line1 = lines[i].rstrip()	# remove trailing \n
			out_line = 'rm ' + '"' + out_line1 + '"' + '\n'
							#add a \n after the closing quote
			if len (out_line) > 6:		# don't write out rm ""\n, Nigel!
				text_file.write(out_line)

text_file.close()
