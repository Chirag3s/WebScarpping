from selenium import  webdriver
from selenium.webdriver.common.by import By
import time

# Importing Selenium Webdriver and By to access the browser and html and elements and time for loading the page

driver = webdriver.Chrome()
# Accessing The Browser

urls=[
    "https://www.linkedin.com/jobs/search?location=India&geoId=102713980&f_C=1035&position=1&pageNum=0",
    "https://www.linkedin.com/jobs/search?keywords=&location=India&geoId=102713980&f_C=1441",
    "https://www.linkedin.com/jobs/search?keywords=&location=India&geoId=102713980&f_TPR=r86400&f_C=1586&position=1&pageNum=0",
]
# Given URL's are stored in List

file = 0
# Variable for naming the files with default value as 0

for url in urls:
    #looping the urls
    driver.get(url)
    # accessing the urls one by one
    driver.implicitly_wait(10)
    # waiting for the pages to be loaded
    job_details = driver.find_elements(By.CLASS_NAME,"job-search-card")
    # Storing the job details by accessing the html elements using class name
    for jd in job_details:
        # looping the list of job_details
        data = jd.get_attribute("outerHTML")
        # storing the outerHTML data of all pages
        with open(f"JOBDETAILS/MGA_{file}.html","w",encoding="utf-8")as f:
            # opening the files one by one to store the respective page data
            f.write(data)
            # writing the pages
            file+=1
            # incrementing the value by 1

time.sleep(2)

driver.quit()
# closing the Browser