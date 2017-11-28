#! /usr/bin/python3
import requests, json, argparse, sys

def ipDefault(ipquery=""):
	url = "http://ip-api.com/json/" + ipquery
	req = requests.get(url)
	json_obj = req.json()

	ip = json_obj['query']
	print(ip)

def ipFull(ipquery=""):
	url = "http://ip-api.com/json/" + ipquery
	req = requests.get(url)
	json_obj = req.json()

	ip = json_obj['query']
	isp = json_obj['isp']
	asn = json_obj['as']
	city = json_obj['city']
	region = json_obj['region']
	regionname = json_obj['regionName']
	country = json_obj['country']
	zipcode = json_obj['zip']
	print(ip)
	print(isp)
	print(asn)
	print(country)
	print(regionname + " (" + region + ")")
	print(city)
	print(zipcode)








def helpMenu():
	print("USAGE: python3 " + sys.argv[0] + " <ip> [OPTIONS]")
	print()
	print("-h,  --help     Shows options of this program")
	print("-f,  --full     Displays information about IP, (isp, asn, country, etc.)")
	print("-s,  --self     IP of machines network")


if(len(sys.argv) < 2):
	print("INCORRECT USAGE!")
	helpMenu()
elif(len(sys.argv) ==  2):
	if(sys.argv[1] == '-s' or sys.argv[1] == '--self'):
		ipDefault()
	elif(sys.argv[1] == '-s' or sys.argv[1] == '--self'):
		helpMenu()
	elif("." in sys.argv[1]):
		ipDefault(sys.argv[1])
	else:
		helpMenu()

elif(len(sys.argv) == 3):
	if(("." in sys.argv[1]) and (sys.argv[2] == "-f" or sys.argv[2] == "--full")):
		ipFull(sys.argv[1])
	elif((sys.argv[1] == "-s" and sys.argv[2] == "-f") or (sys.argv[1] == "-f" and sys.argv[2] == "-s")):
		ipFull()
	elif((sys.argv[1] == "--self" and sys.argv[2] == "--full") or (sys.argv[1] == "--full" and sys.argv[2] == "--self")):
		ipFull()
	else:
		helpMenu()
else:
	helpMenu()