import requests 

def check(): 
    r = requests.get("https://ipinfo.io/")
    if r.status_code == 200:
        print("\n[+] Server Online!\n")
    else:
        print("\n[!] Server Offline!\n")
        exit()

ip = input("Welche IP willst du abfragen: ")

check()

country = requests.get("https://ipinfo.io/{}/country/".format(ip)).text
city = requests.get("https://ipinfo.io/{}/city".format(ip)).text
region = requests.get("https://ipinfo.io/{}/region/".format(ip)).text
postal = requests.get("https://ipinfo.io/{}/postal/".format(ip)).text
timezone = requests.get("https://ipinfo.io/{}/timezone/".format(ip)).text
orgination = requests.get("https://ipinfo.io/{}/org/".format(ip)).text
location = requests.get("https://ipinfo.io/{}/loc".format(ip)).text

print("IP: "+ip)
print("Land: "+country)
print("Stadt: "+city)
print("Bundesstaat: "+region)
print("PLZ: "+postal)
print("Zeitzone: "+timezone)
print("Anbieter: "+orgination)
print("Standort: "+location)
