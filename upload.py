from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys, csv


driver = webdriver.Chrome()
url = sys.argv[1]
email_file = sys.argv[2]

with open(email_file) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    for row in readCSV:
        email = row[0]
        driver.get(f"{url}")
        driver.execute_script(f"document.getElementsByClassName('quantumWizTextinputPaperinputInput exportInput')[0].value = '{email}'")
        driver.execute_script("document.getElementsByClassName('quantumWizButtonPaperbuttonLabel exportLabel')[0].click()")
        sleep(.5)
driver.close()




