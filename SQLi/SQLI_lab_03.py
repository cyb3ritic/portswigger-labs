# SQL injection attack, querying the database type and version on Oracle

import requests, sys, urllib3
from bs4 import BeautifulSoup as bs

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


if __name__ == '__main__':
    