import socket
import threading

localIP     = "0.0.0.0"
localPort   = 20001
bufferSize  = 40960

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Bind to address and ip
UDPServerSocket.bind((localIP, localPort)) 
print("Server up and listening\n")


# Listen for incoming datagrams
while(True):	    
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    original = message.decode("utf-8")
    
    # adding overhead computation
    i=0
    j=0
    while(i<50):
    	original = original[::-1]
    	j += pow(0.123456, i)
    	i+=1

    x = [0]*4096
    sum = 0
    for i in range(0,4095):
    	sum+= x[i]
    	sum*= x[i]

    clientMsg = "Message from Client :" + (original)
    # print(clientMsg)

    bytesToSend = str.encode("LE WAPIS " + (original[::-1]))
    UDPServerSocket.sendto(bytesToSend, address)
