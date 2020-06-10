#!/bin/bash

while IFS= read -r line
do
    nmap -sV --script ssl-enum-ciphers -p 443 $line >> certgrader.txt
done < "tmp4.txt"
