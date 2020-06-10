#!/bin/bash

for i in $(cat cves_uniq.txt)
do
	curl https://www.cvedetails.com/cve/$i/?q=$i | grep 'name="keywords" content=' >> tmp2.txt 
done
