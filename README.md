# shodan_tools

#SETUP

	0) Make sure nmap is installed 

	1) Make sure all .sh files can be executed (cmhod +x <file>)

	2) Save IPv4 addresses in file called "iprange.txt" with one address per line
	
	3) run.sh or run2.sh

	4) run tools (parse.py, get_cves.py, certgrader.py)


#Tools do the following:

*  parse.py 
	takes a keyword and searches shodan output, lists all shodan output & list of IPs via parsed data
		ex 
			python parse.py <keyword>

*  get_cves.py
	Takes shodan output, greps on all found CVEs, cleans it up and returns the following:
		1) all found cves
		2) all unique cves ranked by database search (severity)

*  certgrader.py
	runs certgrader, uses nmap to check all ssl-enum-ciphers

*  run.sh
	Runs shodan host search (free but may be outdated or unchecked)

*  run2.sh
	Runs shodan search (up to date & checked but expensive)
