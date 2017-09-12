# Tool 	        	: Webserver_Version_Exposure.py
# Author		: Mayendran Govender
# Date Created          : 23 July 2015
# Description		: This tool scans  your webserver to determine if you are exposing the version details. Exposing the web server version details could allow attackers to easily find vulnerabilities relating to you version of webserver in use.  
# Usage                 : python Webserver_Version_Exposure.py 

###########Important Notice - Please test this Tool in a test platorm and understand how this tool works before using in a production platform. 

###########Modules Loaded
import platform		                # Loading the list of  Modules
import os
import subprocess
import sys

import subprocess
print "Please check output below to determine if you are exposing the webserver version"
subprocess.call('HEAD www.example.com | grep "Server"' ,   shell=True) # change example.com to your domain  name 
