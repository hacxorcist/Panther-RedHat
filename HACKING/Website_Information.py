#!/usr/bin/python2
import os
import time
import sys
import fileinput
from dm import *
import commands

def main_website_info():
	p=1
	os.system("touch hackfiles/temp")
	try:	
		while p!=0:
			os.system("dialog --ascii-lines --backtitle 'ThE PaNtHeR' --title  'WEBSITE INFORMATION' --menu  'Select an Option' 25 60 6 1 'IP Address of any website using nslookup ' 2 'DIG-Domain Information Groper' 3 'Website information using Host Command ' 4 'Whois command to know more about a public IP' 5 'Google Hacking-Extract info using Google Search'  2> hackfiles/temp")
			fh=open("hackfiles/temp", "r")
			ch=fh.read()
			fh.close()
			if ch=="":
				break
			elif int(ch)==1:
				nslookup()
			elif int(ch)==2:
				dig()
			elif int(ch)==3:
				host()
			elif int(ch)==4:
				whois()
			elif int(ch)==5:
				ghack()
			else:
				pass
	except:
		error()
		pass

def nslookup():
	try:
		inputbox("Enter the IP/Website Name:-","15","60","hackfiles/temp")
		fh=open("hackfiles/temp", "r")
		web=fh.read().strip()
		fh.close()
		if web!="":
			os.system("nslookup "+web+" > hackfiles/temp")
			textbox("hackfiles/temp","40","100")
	except:
		error()
		pass
		
def dig():
	try:
		inputbox("Enter the IP/Website Name:-","15","60","hackfiles/temp")
		fh=open("hackfiles/temp", "r")
		web=fh.read().strip()
		fh.close()
		if web!="":
			os.system("dig "+web+" +nocomments > hackfiles/temp")
			textbox("hackfiles/temp","40","100")
	except:
		error()
		pass

def host():
	try:	
		inputbox("Enter the IP/Website Name:-","15","60","hackfiles/temp")
		fh=open("hackfiles/temp", "r")
		web=fh.read().strip()
		fh.close()
		if web!="":
			os.system("host "+web+" &> hackfiles/temp")
			textbox("hackfiles/temp","40","100")
	except:
		error()
		pass

def whois():
	try:
		inputbox("Enter the IP/Website Name:-","15","60","hackfiles/temp")
		fh=open("hackfiles/temp", "r")
		web=fh.read().strip()
		fh.close()
		os.system("whois "+web)
		wait()
	except:
		error()
		pass

def traceroute():
	try:
		inputbox("Enter the IP/Website Name:-","15","60","hackfiles/temp")
		fh=open("hackfiles/temp", "r")
		ip=fh.read().strip()
		fh.close()
		if ip!="":
			os.system("traceroute "+ip+" &> hackfiles/temp")
			textbox("hackfiles/temp","30","120")
	except:
		error()
		pass

def ghack():
	p=1
	os.system("touch confiles/config")
	while p!=0:
		try:
			os.system("dialog --ascii-lines --backtitle 'ThE PaNtHeR' --title  'Extact Website info via GOOGLE SEARCH' --menu  'Select an Option' 25 60 6 1 'Search for Subdomains of a site' 2 'Search within a Site' 3 'Search for a particular filetype within a site' 4 'Search for a query on Google' 2> hackfiles/temp")
			fh=open("hackfiles/temp", "r")
			ch=fh.read()
			fh.close()
			if ch=="":
				break
			elif int(ch)==1:
				inputbox("Enter Website name:-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				web=fh.read().strip()
				fh.close()
				if web!="":
					query=web+" -site:www."+web
					os.system(" firefox http://www.google.com/search?hl=en#q="+`query`)
			elif int(ch)==2:
				inputbox("Enter Website name:-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				web=fh.read().strip()
				fh.close()
				if web!="":
					inputbox("Enter a string to search within "+web+" :-","15","60","hackfiles/temp")
					fh=open("hackfiles/temp", "r")
					query=fh.read().strip()
					fh.close()
					if quer!="":
						os.system("firefox http://www.google.com/search?hl=en#q=site:"+`web+" "+query`)
			elif int(ch)==3:
				inputbox("Enter Website name:-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				web=fh.read().strip()
				fh.close()
				if web!="":
					inputbox("Enter a filetype to search within "+`web`+" :-","15","60","hackfiles/temp")
					fh=open("hackfiles/temp", "r")
					filetype=fh.read().strip()
					fh.close()
					if filetype!="":
						os.system("firefox http://www.google.com/search?hl=en#q=site:"+`web+" filetype:"+filetype`)
			elif int(ch)==4:
				inputbox("Enter Query:-","15","60","hackfiles/temp")
				fh=open("hackfiles/temp", "r")
				query=fh.read().strip()
				fh.close()
				if query!="":
					os.system("firefox http://www.google.com/search?hl=en#q="+`query`)
			else:
				pass
		except:
			error()
			pass
#main_website_info()
