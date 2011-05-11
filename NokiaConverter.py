import sys
infile = open('/home/ankit/Mukesh.vcf','r')
outfile = open('/home/ankit/MukeshContacts.txt','w')
lines = infile.readlines()
counter = len(lines)
print(counter)
for i in range(0,counter):
    blanker = 9
    liner = 0
    if (lines[i].startswith('N:')):
        lines[i]= lines[i].partition('N:')
        lines[i] = lines[i][2]
        outfile.write(lines[i])
        liner += 1
        for incount in range(i-3,i):
            if (lines[incount].startswith('TEL;')):
                print('Haha')
                lines[incount]= lines[incount].partition(':')
                lines[incount]=lines[incount][2]
                outfile.write(lines[incount])
                liner += 1
        for incounter in range(liner,blanker):
            outfile.write('\n')
