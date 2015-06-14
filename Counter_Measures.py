import os

def ctm():
    os.system('dialog --checklist "Select the Counter-Measures:" 10 40 3 \
        1 "Force SYN packets check" off \
        2 "Limit SYN Flood" off \
        3 "Block XMAS scan" off 2> choice')
    fch = open("choice",'r')
    ch = fch.readline()
    fch.close()
    if ch == '1':
        os.system('iptables -A INPUT -p tcp ! --syn -m state --state NEW -j DROP')
        os.system('dialog --title "Message" --msgbox "Force check is on!!" 15 40')
    elif ch == '2':
        os.system('dialog --inputbox "Enter the number of SYN packets per second to be accepted:" 10 40 --and-widget 2>  choice')
        h= open("choice",'r')
        limit=int(h.readline())
	h.close()
        os.system('iptables -A INPUT -p tcp --syn -m limit --limit '+ str(limit)+'/s --limit-burst '+ str(limit+5)+' -j DROP')
        os.system('dialog --title "Message" --msgbox "Applied limit on  SYN packets!!" 15 40')
    elif ch == '3':
        os.system('iptables -A INPIT -p tcp --tcp-flags ALL NONE -j DROP')
        os.system('iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP')
        os.system('dialog --title "Message" --msgbox "XMAS scan blocked!!" 15 40')
    elif ch == '1 2':
        os.system('iptables -A INPUT -p tcp ! --syn -m state --state NEW -j DROP')
        os.system('dialog --title "Message" --msgbox "Force check is on!!" 15 40')
        os.system('sleep 3')
        os.system('dialog --inputbox "Enter the number of SYN packets per second to be accepted:" 10 40 --and-widget 2>  choice')
        h= open("choice",'r')
        limit=int(h.readline())
	h.close()
        os.system('iptables -A INPUT -p tcp --syn -m limit --limit '+ str(limit)+'/s --limit-burst '+ str(limit+5)+' -j DROP')
        os.system('dialog --title "Message" --msgbox "Applied limit on  SYN packets!!" 15 40')
    elif ch == '1 3':
        os.system('iptables -A INPUT -p tcp ! --syn -m state --state NEW -j DROP')
        os.system('dialog --title "Message" --msgbox "Force check is on!!" 15 40')
        os.system('sleep 3')
        os.system('iptables -A INPIT -p tcp --tcp-flags ALL NONE -j DROP')
        os.system('iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP')
        os.system('dialog --title "Message" --msgbox "XMAS scan blocked!!" 15 40')
    elif ch == '2 3':
        os.system('dialog --inputbox "Enter the number of SYN packets per second to be accepted:" 10 40 --and-widget 2>  choice')
        h= open("choice",'r')
        limit=int(h.readline())
	h.close()
        os.system('iptables -A INPUT -p tcp --syn -m limit --limit '+ str(limit)+'/s --limit-burst '+ str(limit+5)+' -j DROP')
        os.system('dialog --title "Message" --msgbox "Applied limit on  SYN packets!!" 15 40')
        os.system('sleep 2')
        os.system('iptables -A INPIT -p tcp --tcp-flags ALL NONE -j DROP')
        os.system('iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP')
        os.system('dialog --title "Message" --msgbox "XMAS scan blocked!!" 15 40')
    elif ch == '1 2 3':
        os.system('iptables -A INPUT -p tcp ! --syn -m state --state NEW -j DROP')
        os.system('dialog --title "Message" --msgbox "Force check is on!!" 15 40')
        os.system('sleep 2')
        os.system('dialog --inputbox "Enter the number of SYN packets per second to be accepted:" 10 40 --and-widget 2>  choice')
        h= open("choice",'r')
        limit=int(h.readline())
	h.close()
        os.system('iptables -A INPUT -p tcp --syn -m limit --limit '+ str(limit)+'/s --limit-burst '+ str(limit+5)+' -j DROP')
        os.system('dialog --title "Message" --msgbox "Applied limit on  SYN packets!!" 15 40')
        os.system('sleep 2')
        os.system('iptables -A INPIT -p tcp --tcp-flags ALL NONE -j DROP')
        os.system('iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP')
        os.system('dialog --title "Message" --msgbox "XMAS scan blocked!!" 15 40')


if __name__=="__main__":
    ctm()
