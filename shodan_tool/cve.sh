#!/bin/bash

for i in $(cat cve_all.txt)
do
	#curl https://www.cvedetails.com/cve/$i/?q=$i | grep 'name="keywords" content=' >> tmp2.txt 
	curl https://www.cvedetails.com/cve/$i/?q=$i >> test.txt
	cat test.txt | grep 'name="description" content="' >> description.txt
	cat test.txt | grep 'name="keywords" content=' >> tmp2.txt 
	rm test.txt
done
