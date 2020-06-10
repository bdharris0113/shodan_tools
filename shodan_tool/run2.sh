#!/bin/bash

while IFS= read -r line
do
    shodan scan submit $line >> out3.txt
done < "iprange.txt"
