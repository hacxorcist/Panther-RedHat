#!/usr/bin/python2
import os
import time
import sys
import fileinput
from dm import *

def main_client_install():
	p=1
	os.system("touch confiles/config")
	while p!=0:
		os.system("dialog --ascii-lines  --backtitle 'CLIENT SIDE SOFTWARE INSTALLATION' --menu  'Install Client Side Requirements for :-' 25 60 10 1 'Telnet' 2 'FTP' 3 'SSH' 4 'Web Browser' 5 'Mail' 6 'NIS' 7 'NFS' 8 'Samba' 9 'Autofs' 10 'NTP' 2> confiles/config")
		fhch=open("confiles/config", "r")
		ch=fhch.read()
		fhch.close()
		os.system("setenforce 0")
		os.system("iptables -F")
		if ch=="":
			break
		elif int(ch)==1:
			telnet_client_install()
		elif int(ch)==2:
			ftp_client_install()
		elif int(ch)==3:
			ssh_client_install()
		elif int(ch)==4:
			web_client_install()
		elif int(ch)==5:
			mail_client_install()
		elif int(ch)==6:
			nis_client_install()
		elif int(ch)==7:
			nfs_client_install()
		elif int(ch)==8:
			samba_client_install()
		elif int(ch)==9:
			autofs_client_install()
		elif int(ch)==10:
			ntp_client_install()
		else:
			error()
			pass

def telnet_client_install():
	try:
		var=os.system("rpm -q telnet &> /dev/null")
		if var!=0:
			install("telnet")
		restart("telnet")
		os.system("chkconfig ftp on")
		msgbox("Successfully Installed Telnet Client on the Computer","10","40")
	except:
		msgbox("Error!! Please Contact the Developer","10","40")

def ftp_client_install():
	try:
		var=os.system("rpm -q ftp &> /dev/null")
		if var!=0:
			install("ftp")
		restart("ftp")
		os.system("chkconfig ftp on")
		msgbox("Successfully Installed FTP Client on the Computer","10","40")
	except:
		msgbox("Error!! Please Contact the Developer","10","40")

def ssh_client_install():
	try:
		msgbox("Successfully Installed SSH Client on the Computer","10","40")
	except:
		msgbox("Error!! Please Contact the Developer","10","40")

def web_client_install():
	try:
		var=os.system("rpm -q firefox &> /dev/null")
		if var!=0:
			install("firefox")
		msgbox("Successfully Installed Firefox Browser on the Computer","10","40")
	except:
		msgbox("Error!! Please Contact the Developer","10","40")

def mail_client_install():
	try:
		var=os.system("rpm -q postfix &> /dev/null")
		if var!=0:
			install("postfix")
		restart("postfix")
		os.system("chkconfig postfix on")
		msgbox("Successfully Installed Mail Client on the Computer","10","40")
	except:
		msgbox("Error!! Please Contact the Developer","10","40")

def nis_client_install():
	try:
		var=os.system("rpm -q ypbind &> /dev/null")
		if var!=0:
			install("ypbind")
		restart("ypbind")
		os.system("chkconfig ypbind on")
		msgbox("Successfully Installed NIS Client setup on the Computer","10","40")
	except:
		msgbox("Error!! Please Contact the Developer","10","40")

def nfs_client_install():
	try:
		var=os.system("rpm -q nfs-utils &> /dev/null")
		if var!=0:
			install("nfs-utils")
		restart("postfix")
		os.system("chkconfig nfs on")
		msgbox("Successfully Installed NFS Client Software on the Computer","10","40")
	except:
		msgbox("Error!! Please Contact the Developer","10","40")

def samba_client_install():
	try:
		var=os.system("rpm -q samba-client &> /dev/null")
		if var!=0:
			install("samba-client")
		msgbox("Successfully Installed Samba Service Client Software on the Computer","10","40")
	except:
		msgbox("Error!! Please Contact the Developer","10","40")

def autofs_client_install():
	try:
		var=os.system("rpm -q autofs &> /dev/null")
		if var!=0:
			install("autoserv")
		restart("autofs")
		os.system("chkconfig autofs on")
		msgbox("Successfully Installed autofs Client setup on the Computer","10","40")
	except:
		msgbox("Error!! Please Contact the Developer","10","40")

def ntp_client_install():
	try:
		var=os.system("rpm -q ntp &> /dev/null")
		if var!=0:
			install("ntp")
		restart("ntp")
		os.system("chkconfig ntp on")
		msgbox("Successfully Installed NTP Client setup on the Computer","10","40")
	except:
		msgbox("Error!! Please Contact the Developer","10","40")

#main_client_install()
