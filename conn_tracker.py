import socket, sys, os
from struct import *
import reset
#0x0003 stands for all protocols in ethernet header
try:
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
except socket.error , msg:
    print 'Socket creation failed. Error Code -> ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
def capture():
    fin_count = 0
    state_track=dict()
    print  "Total Number of TCP connections: ",len(state_track)
    print "Key_Value" + " |Source_IP" + " |Destination_IP" + "|S_Port" + "|D_Port" + "|Sequence_No." \
                    + "|Acknowledge_No." + "|Flag"
    print "-------------------------------------------------------------------------------------"
    while True:
        packet = s.recvfrom(65565)
        packet = packet[0]
        #sort out ethernet header
        eth_length = 14
        eth_header = packet[:eth_length]
        eth = unpack('!6s6sH' , eth_header)
        eth_protocol = socket.ntohs(eth[2])
        if eth_protocol == 8:
            ip_header = packet[14:34]
            iph = unpack('!BBHHHBBH4s4s' , ip_header)
            version_ip_hdr_len = iph[0]
            #version = version_ip_hdr_len >> 4
            ip_hdr_len = version_ip_hdr_len & 0xF
            iph_length = ip_hdr_len * 4 
            #ttl = iph[5]
            protocol = iph[6]
            src_addr = iph[8]
            dst_addr = iph[9]
            if str(protocol) == '6':
                tcp_header = packet[14+iph_length:14+iph_length+20]
         
                #now unpack them ->)
                tcph = unpack('!HHLLBBHHH' , tcp_header)
                src_port = tcph[0]
                dst_port = tcph[1]
                seq_no = tcph[2]
                ack_no = tcph[3]
                doff_reserved = tcph[4]
                flag= tcph[5]
                tcph_length = doff_reserved >> 4
                window_size = tcph[6]

# Conn Track
                
                key = unpack('>I',src_addr)[0] + int(src_port) + unpack('>I',dst_addr)[0] + int(dst_port)
                if key not in state_track and str(flag) != '2':
                    print "Invalid state detected. "
                    reset.main(socket.inet_ntoa(dst_addr), socket.inet_ntoa(src_addr), int(dst_port), int(src_port), int(ack_no), int(seq_no+1))
                    pass
                elif key in state_track and str(flag) == '17':
                    state_track[key][7] += 1
                    for key in state_track:
                        print( str(key) + " " +str(state_track[key][0]) + " " + str(state_track[key][1]) + "   " + str(state_track[key][2]) +"    " + str(state_track[key][3]) + "    " + str(state_track[key][4]) + "    " + str(state_track[key][5]) + "      " + str(state_track[key][6]))

                elif key in state_track and  state_track[key][7] == 2 and flag == 16:
                    print "FIN-ACK Acknowledged!! Removing connection entry from data structure for key: "+str(key)
                    print "Total number of connections now is ",len(state_track)
                    del state_track[key]
                    
                else:
                    state_track[key] = [socket.inet_ntoa(src_addr),socket.inet_ntoa(dst_addr),src_port,dst_port,seq_no,ack_no,flag,fin_count]

                    for key in state_track:
                        print( str(key) + " " +str(state_track[key][0]) + " " + str(state_track[key][1]) + "   " + str(state_track[key][2]) +"    " + str(state_track[key][3]) + "    " + str(state_track[key][4]) + "    " + str(state_track[key][5]) + "      " + str(state_track[key][6]))
                    

if __name__=="__main__" :
	capture()
