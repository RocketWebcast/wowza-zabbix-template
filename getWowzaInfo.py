#!/bin/env python
# by Mike Schaefer based on Vicente Dominguez
# -a conn - Global connections
# -a appnum - Global application(streaming) num
# -a uptime - Global uptime
# -a conntotal - Global total connections
# -a inbytes - Global incoming bytes
# -a outbytes - Global outgoing bytes
# -a all - All the above in pipe format

import urllib.request, urllib3, base64, sys, getopt
import xml.etree.ElementTree as ET

# Default values
username = "admin"
password = "admin"
host = "localhost"
port = "8086"
getInfo = "None"

##

def Usage ():
        print("Usage: getWowzaInfo.py -u user -p password -h 127.0.0.1 -P 8086 -a [conn|appnum|uptime|conntotal|inbytes|outbytes|all]")
        sys.exit(2)

def getCurrentConnections():
        print(xmlroot[0].text)

def getTotalConnections():
        print(xmlroot[1].text)

def getCurrentStreams():
        Application =  xmlroot.findall('VHost/Application')
        print(len(Application))
		
def getUptime():
        print(xmlroot.find('VHost').find('TimeRunning').text)

def getInbytes():
        print(xmlroot.find('MessagesInBytesRate').text)

def getOutbytes():
        print(xmlroot.find('MessagesOutBytesRate').text)

def getAll():
	    print(xmlroot.find('VHost').find('TimeRunning').text + "|" + xmlroot.find('MessagesOutBytesRate').text + "|" + xmlroot.find('MessagesInBytesRate').text + "|" + xmlroot[0].text + "|" + xmlroot[1].text + "|" + str(len(xmlroot.findall('VHost/Application'))))

def unknown():
        print("unknown")

##


def main (username,password,host,port,getInfo):

	global xmlroot    
	argv = sys.argv[1:]	
    
	if (len(argv) < 1):
		Usage()   
    
	try :
			opts, args = getopt.getopt(argv, "u:p:h:P:a:")

			# Assign parameters as variables
			for opt, arg in opts :
					if opt == "-u" :
							username = arg
					if opt == "-p" :
							password = arg
					if opt == "-h" :
							host = arg
					if opt == "-P" :
							port = str(arg)
					if opt == "-a" :
							getInfo = arg
	except :
					Usage()


	url="http://" + host + ":" + port + "/connectioncounts/"
 
	http = urllib3.PoolManager()
	http.cache = True
	http.cache_timeout = 30
	http.cache_maxsize = 1000
	http.cache_block = True
	http.cache_storage = True
	http.cache_content = True
	myHeaders = urllib3.util.make_headers(basic_auth=username + ":" + password)
	myHeaders["Authorization"] = "Basic %s" % base64.b64encode(bytes('%s:%s' % (username, password), 'utf-8')).decode('utf-8')
	myHeaders["Content-Type"] = "application/xml"
	myHeaders["Accept"] = "application/xml"
	myHeaders["Cache-Control"] = "public, min-fresh=20, max-age=30 immutable"
	result = http.request('GET', url, headers=myHeaders, timeout=5.0)
	xmlroot = ET.fromstring(result.data.decode('ascii'))
	# print(xmlroot.tag)


	if ( getInfo == "conn"):
			getCurrentConnections()
	elif ( getInfo == "conntotal"):
			getTotalConnections()
	elif ( getInfo == "appnum"):
			getCurrentStreams()
	elif ( getInfo == "uptime"):
			getUptime()
	elif ( getInfo == "inbytes"):
			getInbytes()
	elif ( getInfo == "outbytes"):
			getOutbytes()
	elif ( getInfo == "all"):
			getAll()
	else:
			getAll()



if __name__ == "__main__":

    main(username,password,host,port,getInfo)
