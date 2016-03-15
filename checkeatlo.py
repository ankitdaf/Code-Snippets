# A simple script to run all the numbers in your address book against
# the EatLo database to check which of your friends are EatLo customers,
# and get their addresses.
# 
# It takes a file "phones.csv" as input, where each line contains a 10 digit cellphone number
# 
# @ankitdaf
# 
# You are free to do with this code as you please, I do not assume any credit or liability if you 
# use this. 

import requests,json
url = "http://api.eat-lo.in/backend/BLL/Retrieve/GetCustomers.php"
headers = {"Content-Type": "application/json"}
payload = {}
f=open("phones.csv")
for line in f.readlines():
	payload = {"data":{"MobileNumber":line.strip()}}
	r= requests.post(url,data=json.dumps(payload),headers=headers)
	print line.strip(), r.text