import re
import sys

if len(sys.argv) != 2:
	print "      Usage"
	print "python parse.py <Var>"
	print "where Var is what you want to grep on (eg Vuln, TLS, ...)"
	sys.exit()


f = open('out2.txt')

data = []
for line in f.readlines():
	data.append(line)
f.close()
blocks = []
end = False
for i in range(0,len(data)):
	if end: break	
	block = ''	
	m = re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",data[i])
	if m != None:
		#print m.group()
		block += data[i]
		j = i+1		
		while 1:
			try:
				m2 = re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",data[j])
				if m2 != None:
					break
				block += data[j]
				j += 1
			except:
				end = True
				break

	#print 'block = '+block
	if block != '':
		blocks.append(block)

ips = []
for b in blocks:	
	if str(sys.argv[1]) in b:
		print b
		ip = ''
		for i in b:
			if i in '0123456789.':
				ip += i
			else:
				break	
		ips.append(ip)	
			

print 
print "IP Addresses found with this search:"

for i in ips:
	print i

print 
print "There were " + str(len(ips)) + " found with " + str(sys.argv[1])
