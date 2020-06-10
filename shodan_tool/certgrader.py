import os

os.system("python parse.py 443/tcp | sed -n '/IP Addresses found with this search:/,$p' | head -n -2 | sed -n '1!p' > tmp4.txt")

f = open('tmp4.txt')
data = f.readlines()
f.close()
os.system('./certgrader.sh')
os.system('rm tmp4.txt')







