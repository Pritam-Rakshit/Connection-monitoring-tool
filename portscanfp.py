#!/usr/bin/env python
#!/usr/bin/env python
#import argparse
import socket
import sys
import os
def scan_ports():
	""" Scan remote hosts """
	#Create socket
	try:
                os.system('dialog --menu "Port Scanner" 20 40 2 "1" "FQDN based scanning" "2" "IP based scanning"  2> choice')
                option = open("choice",'r')
                opt = option.readline()
                option.close()
                if opt == '1':
                    os.system('dialog --inputbox "Enter a qualified host name:"  10 40 --and-widget 2>  hostname.txt')
		    h= open("hostname.txt",'r')
		    host=h.readline()
		    h.close()

		    os.system('dialog --inputbox "Enter a starting port Number(Start point of port scan):" 10 40 --and-widget 2>  hostname.txt')
		    h= open("hostname.txt",'r')
		    start_port=int(h.readline())
		    h.close()

		    os.system('dialog --inputbox "Enter a Ending port number(End point of port scan):" 10 40 --and-widget 2>  hostname.txt')
		    h= open("hostname.txt",'r')
		    end_port=int(h.readline())
		    h.close()
	            try:
		#host='tsoft-Vostro-1540'
		        remote_ip = socket.gethostbyname(host)
	#	print remote_ip
	            except socket.error,error_msg:
		        print error_msg
		        sys.exit()
                else:
                    os.system('dialog --inputbox "Enter an IP address:"  10 40 --and-widget 2>  hostname.txt')
		    h = open("hostname.txt",'r')
		    ip =h.readline()
		    h.close()

		    os.system('dialog --inputbox "Enter a starting port Number(Start point of port scan):" 10 40 --and-widget 2>  hostname.txt')
		    h = open("hostname.txt",'r')
		    start_port=int(h.readline())
		    h.close()

		    os.system('dialog --inputbox "Enter a Ending port number(End point of port scan):" 10 40 --and-widget 2>  hostname.txt')
		    h= open("hostname.txt",'r')
		    end_port=int(h.readline())
		    h.close()
	            try:
		#host='tsoft-Vostro-1540'
		        remote_ip = ip
	#	print remote_ip
	            except socket.error,error_msg:
		        print error_msg
		        sys.exit()

	except:
		print "Wrong input data type!"
		sys.exit()


	try:
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                sock.settimeout(8)
	except socket.error,err_msg:
		print 'Socket creation failed. Error code: '+ str(err_msg[0]) + ' Error message: ' + err_msg[1]
		sys.exit()


#Get IP of remote host



#Scan ports
	end_port += 1
	h=open("hostname.txt","w")
	for port in range(start_port,end_port):
		try:
			
			sock.connect((remote_ip,port))
                        sock.timeout(8)
			h.write("Port" + str(port) + " | Service Name:" + socket.getservbyport(port) + "\n")
			#print 'Port ' + str(port) + ' is open'+', Service Name:'+socket.getservbyport(port)
			sock.close()
			sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	
		except socket.error:
			pass # skip various socket errors
	h.close()
	os.system('dialog --title "port Scanner" --textbox hostname.txt 22 70')
	os.system('dialog --backtitle "Message" --radiolist "Do you want to block any service or port?" 10 40 2 1 Yes yes 2 No no 2> choice')
        option = open("choice",'r')
        opt = option.read(1)
        option.close()        
        if opt == '1':
            os.system('dialog --inputbox "Enter the port number to stop:"  10 40 --and-widget 2>  port.txt')
            prt = open("port.txt",'r')
            port = prt.readline()
            prt.close()
            os.system('iptables -t filter -A INPUT -p tcp --dport '+ port +' -j REJECT')
            os.system('iptables -t filter -A INPUT -p udp --dport '+ port +' -j REJECT')
            os.system('dialog --title "Message" --msgbox "Port "'+ port +'" is blocked!" 15 40')
        elif opt == '2':
            os.system('dialog --backtitle "Unblock a Port" --radiolist "Unblock any service or port?" 10 40 2 1 Yes yes 2 No no 2> choice')
            option = open("choice",'r')
            opt1 = option.read(1)
            option.close()
            if opt1 == '1':
                os.system('dialog --inputbox "Enter the port number to stop:"  10 40 --and-widget 2>  port.txt')
                prt = open("port.txt",'r')
                port = prt.readline()
                prt.close()
                os.system('iptables -t filter -D INPUT -p tcp --dport '+ str(port) +' -j REJECT')
                os.system('iptables -t filter -D INPUT -p udp --dport '+ str(port) +' -j REJECT')
                os.system('dialog --title "Message" --msgbox "Port "'+ str(port) +'" is unblocked!" 15 40')
            else:
                sys.exit()
if __name__ == '__main__':	
	scan_ports()
