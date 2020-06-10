#!/bin/bash

while IFS= read -r line
do
    shodan host $line >> out2.txt
done < "iprange.txt"
