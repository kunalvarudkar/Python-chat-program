from socket import * #library for using socket programming
import netifaces as ni   # library for getting localhost ip address

#host=raw_input("Enter your IP Address=")
port=50000 #deafult port no

soc=socket(AF_INET,SOCK_STREAM)  #defined transmission mechanism ans type of protocol
soc.setsockopt(SOL_SOCKET,SO_REUSEPORT,1) #defined the socket options

# menu driven
choice=input("1. Want to be Server\n2. Want to be Cient\nEnter your choice=")
if choice==1:

     #getting our localhost ip address
    ni.ifaddresses('eth0')
    host = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']  #storing in variable "host"

    print "Server IP:"+str(host)
    soc.bind((host, port)) #binding host and port
    soc.listen(1)  #listening to only single request from client
    print("listening on port:" + str(port))
    print ("waiting for incoming connction.....")

    while True: #infinite loop
        c,addr=soc.accept() #accepting the conn form client
        print("Got connection from:"+str(addr[0])+"at Port No:"+str(addr[1]))
        c.send("Your are connected to" +str(host))

        while True:
            temp_buff = raw_input("Server:")  #create temp buffer for sending messages !
            if temp_buff == 'end': #checking the terminaltion WORD ->"END"
                exit()
            else:
                c.send(temp_buff)
                temp_buff=""  #flushing to NULL
                cmsg=c.recv(4028)
                if cmsg=='end':
                    exit()
                else:
                    print "CLIENT:"+str(cmsg)
            #c.close()

elif choice==2:
    host=raw_input("Enter server's IP address to connect=")
    #print "Sending request to:"+host
    soc.connect((host,port))

    print soc.recv(4028)
    while True:
     temp_buff=raw_input("Client:")
     if temp_buff == 'end':
        exit()
     else:
         soc.send(temp_buff)
         temp_buff=""
         smsg=soc.recv(4028)
         if smsg == 'end':
             exit()
         else:
            print "SERVER:"+str(smsg)
    #soc.close()

else :
    exit()