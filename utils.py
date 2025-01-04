import re
import requests
import sys
from bs4 import BeautifulSoup
import pandas
import os

session = requests.Session()



def load_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Accept-Language': 'en-US, en;q=0.5'}
    try:
        r = session.get(url=url, headers=headers)
        if r.status_code == 200:
            return r
    except Exception as e:
        print("Something wrong.", e)


def extract_page(url):
    print(f"Is scraping data at Lawyer profile : {url}")
    r = load_page(url)
    dftemp = pandas.DataFrame()
    try:
        soup = BeautifulSoup(r.content, features="html.parser")
        containers = soup.find_all("div", class_="fieldSubContainer labeledTextContainer")
        mydict = dict()
        for container in containers:
            mylist = [label for label in container.getText().split("\n") if label != '']
            mydict[mylist[0]] = mylist[1]
        if containers.__len__() == 0:
            print(f"The page html has change element structure.")
            raise Exception
        #     get the element not exist in keys
        intersection1 = [key for key in mydict.keys()]
        intersection2 = ["First name", "Last name", "Phone", "e-Mail"]
        not_exist_field = [i for i in intersection2 if i not in intersection1]
        # set empty for field not exist
        for element in not_exist_field:
            mydict[element] = ""
        dftemp = pandas.DataFrame({"First name": [mydict["First name"]], "Last name": [mydict["Last name"]],"Phone": [mydict["Phone"]], "e-Mail": [mydict["e-Mail"]]})
    except Exception as e:
        print(f"Something wrong with this member:{url}")
        pass
    finally:
        return dftemp



def get_file_name():

    filename = f"Find-lawyer.csv"
    if os.name == "nt":
        # window
        filepath = os.getcwd() + "\\output\\" + filename
    else:
        # other
        filepath = os.getcwd() + "/output/" + filename
    return filename, filepath

