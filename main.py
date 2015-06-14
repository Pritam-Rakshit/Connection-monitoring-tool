import os, portscanfp
import Conn_tracker
import Counter_Measures

def main():
    os.system('dialog --menu "Connection Monitoring Tool" 20 40 4 "1" "Port Scanner" "2" "Connection Tracker" "3" "Counter-Measures" 2> choice')

    fch = open("choice",'r+')
    ch = fch.read(1)
    fch.close()
    if ch == "1":
        portscanfp.scan_ports()
    elif ch == "2":
        os.system('clear')
        Conn_tracker.capture()
    elif ch == "3":
        Counter_Measures.ctm()

if __name__=="__main__":
    main()
