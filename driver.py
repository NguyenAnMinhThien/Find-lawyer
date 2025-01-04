import webbrowser
import selenium
import time
import pandas
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium import webdriver
from utils import get_file_name, extract_page

global Total_results
def move_next_range(driver, select):
    ActionChains(driver) \
        .move_to_element(select) \
        .click_and_hold() \
        .key_down(Keys.ARROW_DOWN) \
        .key_down(Keys.ENTER) \
        .pause(2) \
        .perform()
    ActionBuilder(driver).clear_actions()
def get_member_urls():
    driver = webdriver.Chrome()
    members_url = list()
    # driver.get('https://macdl.com/find-a-lawyer/')
    # need to redirect to this page before scrape
    driver.get('https://members.macdl.com/widget/find-lawyer')

    # driver.implicitly_wait(10)
    time.sleep(4)
    Total = driver.find_element(By.ID,"membersFound").text
    Total_result = int(Total.strip())
    print(f"The results found: {Total_result}")
    result_per_page = 50
    count = 0
    while( count < (Total_result // result_per_page + 1)):
        select = driver.find_element(By.TAG_NAME, "select")
        clickable = driver.find_elements(By.CSS_SELECTOR, "a[title='Go to member details']")
        get_urls = [members.get_attribute("href") for members in clickable ]
        members_url = members_url + get_urls
        move_next_range(driver,select)
        count = count + 1
    return Total_result, members_url

def get_dataframe(members_url,Total_results):
    count = 1
    dftemps = pandas.DataFrame()
    for member_url in members_url:
        print(f"The entry: {count}/{Total_results} ...")
        dftemp = pandas.DataFrame()
        dftemp = extract_page(member_url)
        if not dftemp.empty:
            dftemps = dftemps._append(dftemp, ignore_index= True)
        count = count + 1
    return dftemps
