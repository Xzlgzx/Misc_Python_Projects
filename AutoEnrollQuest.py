from selenium import webdriver
import winsound
import tkinter
from tkinter import messagebox
import time
import os
from datetime import datetime

## This code automatically enrolls the first course currently in the shopping
## cart on the Waterloo class registration system "Quest."


def notification(status):
    root = tkinter.Tk()
    root.withdraw()
    if status == 's':
        messagebox.showinfo("Success", "Course enrolled.")
    else:
        messagebox.showinfo("Failed", "Please check exception.")
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 1000  # Set Duration To 1000 ms == 1 second
    while True:
        winsound.Beep(frequency, duration)
        time.sleep(1)


driver_path = r'C:\Users\Administrator\PycharmProjects\PyTrademark\chrome_driver\chromedriver.exe'
prompt = input('enter 1 if during the day, 0 during the night')
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://adfs.uwaterloo.ca/adfs/ls/idpinitiatedsignon.aspx?LoginToRP=urn:quest.ss.apps.uwaterloo.ca')
time.sleep(75)
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
counter = 0
while True:
    counter += 1
    try:
        if counter == 750:
            time.sleep(150)
        check = 'CLOSE' not in str(driver.find_element_by_xpath("//img[@width='16' and @height='16' and @style='vertical-align:middle;text-align:center;margin-left:12px']").get_attribute('src'))
        if check:
            driver.find_element_by_css_selector('#DERIVED_REGFRM1_LINK_ADD_ENRL\$82\$').click()
            time.sleep(5)
            driver.find_element_by_css_selector('#DERIVED_REGFRM1_SSR_PB_SUBMIT').click()
            time.sleep(30)
            if not int(prompt):
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            else:
                notification('s')
        time.sleep(2)
        driver.find_element_by_link_text('Add').click()
        time.sleep(5)
    except Exception as e:
        print('##########################################')
        print(e)
        print('##########################################')
        print('Time that exception occurred:',datetime.now())
        if int(prompt):
            notification('f')
