import optparse
from socket import *
from threading import *
screenLock = Semaphore(value=1)
  
def connScan(tgtHost, tgtPort):
	try:
		connSkt = socket(AF_INET, SOCK_STREAM)
		connSkt.connect(tgtHost, tgtPort)
		connSkt.send('Violent Python\r\n')
		results = connSkt.recv(100)
		screenLock.acquire()

		print '[+]%d/tcp open' % tgtPort
		print '[+] ' + str(results)
	except:

		screenLock.acquire()
		print '[-]%d/tcp closed ' % tgtPort

	finally:
		screenLock.release()
		connSkt.close()

def portScan(tgtHost, tgtPorts):

	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print " cannot resolve '%s': Unknown Host"%tgtHost
		return
	
	try:
		tgtName = gethostbyaddr(tgtIP)
		print'\n[+] Scan results for : ' + tgtName[0]
	except:
		print '\n[+] Scan results for ' + tgtIP

	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		#print 'Scanning port ' + port
		t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
		t.start()
		

def main():
	parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
	parser.add_option('-H', dest='tgtHost', type='string', help='specificy target host')

	parser.add_option('-p', dest='tgtPort', type='string', help='specificy target port[s] ')

	(options, args) = parser.parse_args()

	tgtHost = options.tgtHost
	#print args	
	#print options
	#print options.tgtPort
	tgtPorts = str(options.tgtPort).split(',')
	#print tgtPorts

	if (tgtHost == None) | (tgtPorts[0] == None):
		print parser.usage
		exit(0)
	portScan(tgtHost, tgtPorts)

if __name__ == "__main__":
	main()