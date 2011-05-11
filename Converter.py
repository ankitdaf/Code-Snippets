import sys
infile = open('/media/E/Backups/Backup.vcf','r')
outfile = open('/media/E/Backups/Ready.txt','w')
lines = infile.readlines()
counter = len(lines)
print(counter)
for i in range(0,counter):
    blanker = 9
    liner = 0
    if (lines[i].startswith('N:;')):
        lines[i]= lines[i].partition('N:;')
        lines[i] = lines[i][2]
        outfile.write(lines[i])
        liner += 1
        for incount in range(i-6,i-1):
            if (lines[incount].startswith('TEL;')):
                lines[incount]= lines[incount].partition(':')
                lines[incount]=lines[incount][2]
                outfile.write(lines[incount])
                liner += 1
            if (lines[incount].startswith('BDAY:')):
                lines[incount]= lines[incount].partition(':')
                lines[incount]=lines[incount][2]
                bday=lines[incount]
                bday = bday[6:8] +  '-' + bday[4:6] + '-' + bday[0:4] + '\n'              
                outfile.write(bday)
                liner += 1
        for incounter in range(liner,blanker):
            outfile.write('\n')

    if (lines[i].startswith('N:')):
        lines[i]= lines[i].partition('N:')
        lines[i] = lines[i][2]
        lines[i]=lines[i].split(';')
        lines[i][1] = lines[i][1].rstrip();
        lines[i]=lines[i][1] + ' ' + lines[i][0] + '\n'
        #lines[i] = lines[i].capitalize
        outfile.write(lines[i])
        liner += 1
        for incount in range(i-6,i-1):
            if (lines[incount].startswith('TEL;')):                
                lines[incount]= lines[incount].partition(':')
                lines[incount]=lines[incount][2]
                outfile.write(lines[incount])
                liner += 1
            if (lines[incount].startswith('BDAY:')):
                lines[incount]= lines[incount].partition(':')
                lines[incount]=lines[incount][2]
                bday=lines[incount]
                bday = bday[6:8] +  '-' + bday[4:6] + '-' + bday[0:4] + '\n'
                outfile.write(bday)
                liner += 1
        for incounter in range(liner,blanker):
            outfile.write('\n')


    
