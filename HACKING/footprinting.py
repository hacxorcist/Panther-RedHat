##########################################################
Reconnaisance+Footprinting:
A. Network Information:-
	1. Ifconfig/ip addr
	2. ping certain website 
	   ping -c 3 your_domain_name.com 
		change ttl value - ping ip -t time
		change size - ping ip -s sizeinbytes
	3. Traceroute 
	4. know your gateway- route -n or netstat -r or ping 8.8.8.8 -t 1
	5. know your IP address: hostname -I
	6. Know your MAC Address: /sbin/ifconfig | grep 'wlan0'| tr -s ' ' | cut -d ' ' -f5
B. Website information:-
	1. IP Address of any website:- nslookup
	2. DIG domain information groper: dig redhat.com +nocomments 
	3. Host redhat.com or host -v redhat.com
	4. Whois command
	5. Google Hacking
##########################################################
NETWORK SCANNING :

1. nmap network scanning:: nmap -A 192.168.1.11 -n 
	Script to see which hosts are up:-
	for ip in 192.168.1.{1..15}; do ping -t 1 -c 1 $ip > /dev/null && echo "${ip} is up"; done
	nmap -sP 192.168.1.1-255
2. arp -a all computers in LAN
3. change ip address
4. change mac address:- service NetworkManager down
			service network down
			ifdown wlan0
			ifconfig eth0 hw ether macaddress
			ifup eth0
5. HPING-making our own custom packets hping
##########################################################
SNIFFING:
	packet capturing tcpdump/tshark
##########################################################
IPTABLES AND SECURITY:
1. ACL
2. Firewall
3. SeLinux
4. TCP Wrapper
5. Change port no. of a service:- /etc/services
##########################################################
ATTACKS:
1. MITM Attack/ARP poisoning=
			echo 1 > /proc/sys/net/ipv4/ip_forward
			echo 1 > /etc/sysct1.conf
			iptables -A FORWARD -j DROP
2. Phishing Attack
3. DOS ATTACK
##########################################################
'''
