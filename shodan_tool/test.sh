#!/bin/bash

curl https://www.cvedetails.com/cve/CVE-2019-9640/?q=CVE-2019-9640 >> test.txt
cat test.txt | grep 'name="description" content="' >> description.txt
cat test.txt | grep 'name="keywords" content=' >> tmp2.txt 
rm test.txt
