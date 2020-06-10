'''
	gets cves, parses them then removes duplicates
	stores data in 
'''



import os
import re

os.system('python parse.py Vuln | grep Vuln > tmp.txt')

f = open('tmp.txt','rw')

data = f.readlines()
f.close()
os.system('rm tmp.txt')

ret = []

for line in data:
	line = line[25:]
	line = line.split('\t')
	ret += line
		
while (ret.count('\n')):
	ret.remove('\n')
ret.remove('Vuln\n')

uniq = []

for c in ret:
	if c not in uniq:
		uniq.append(c)

f = open('cve_all.txt','w')
for i in uniq:
	f.write(str(i))
	f.write('\n')
f.close()


'-----------------------------------------------------------'

#get all rankings from internet & store in tmp2

os.system('./cve.sh')

'-----------------------------------------------------------'

#sort and rank cves

f = open('tmp2.txt')

data = f.readlines()
f.close()

cves = {}

for line in data:
	try:
		cve = re.search('content="(.*), ',line)
		cve = cve.group(1).split(',')[0]
		rank = re.search('CVSS (.*)"',line)
		rank = float(rank.group(1).split(',')[0])
		cves.update({cve:rank})
		#print cves
	except:
		pass
		
cves_sorted = sorted(cves.items(),key=lambda x: x[1])

f = open('cve_ranked.txt','w')
for i in cves_sorted:
	line = str(i[0]) + ' '+ str(i[1])
	f.write(str(line))
	f.write('\n')
f.close()
