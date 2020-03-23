import socket
import time
import threading

rate = 5000 #per second
total = rate*1200
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.settimeout(10)
msgFromClient       = "LE PACKET"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("Assgn1-LB-9-a9ed2c5516e8bbe0.elb.us-east-1.amazonaws.com", 20000)
bufferSize          = 40960
starts 				= []
ends 				= []
fname = "rate_AS_" + str(rate) + ".txt"
file = open(fname, 'w')
file2 = open("output.txt", 'a')

def receiver():

	global UDPClientSocket
	global ends
	global duration
	global file
	global total
	j=0
	while(j<total):
		try:
			msgFromServer = UDPClientSocket.recvfrom(bufferSize)
		except:
			break
		msg = "Message from Server: {}".format(msgFromServer[0].decode("utf-8"))
		# print(msg + "    " +str(j))
		# print (str(j))
		ends += [time.time()]
		j+=1
	

# Create a UDP socket at client side

i = 0
thread = threading.Thread(target=receiver)
thread.daemon = True
thread.start()
first = time.time()
delay = 1/rate
if(delay <= 0.000001):
	delay = delay*0.1
if(delay <= 0.0001): 
	delay = delay*0.5

while(i<total):
	# Send to server using created UDP socket
	t_in = time.time();
	try:	
		UDPClientSocket.sendto(bytesToSend, serverAddressPort)
	except:
		break
	starts += [time.time()]
	i+=1
	# while(time.time()-t_in < delay):
	# 	continue
	time.sleep(1/rate);

print('done send')
last = time.time()
thread.join()

avg = 0
for x in range(0,len(ends)-1):
	dur = ends[x]-starts[x]
	file.write(str(dur) + "\n")
	avg += dur

avg /= len(ends)
file2.write(str(rate) + ", " + str(avg) + "\n")
# file2.write(str(rate) + ", total " + str(last-first) + "\n")
file.close()
file2.close()
