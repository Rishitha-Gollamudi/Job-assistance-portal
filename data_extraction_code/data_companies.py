from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService 
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager 
import time
import re

import json
from statistics import mean

def company_data(role,loc):
    
    if len(role.split()) > 1:
        role = role.replace(" ", "+")
    if len(loc.split()) > 1:
        loc = loc.replace(" ", "+")

    print(role, loc)
    y=f'https://www.simplyhired.com/search?q={role}&l={loc}'
    print(y)
    # driver = webdriver.Chrome(service=ChromeService( ChromeDriverManager().install())) 
    driver = webdriver.Chrome('C:\\chromedriver.exe')  #################################CHANGE THIS######################
    driver.get(y)
    driver.set_window_size(1920, 1080)
    
    time.sleep(5)

    cnt_pages= driver.find_element("xpath",'/html/body/div[1]/main/div/div[3]/div/div/div[1]/div/div[2]/div[1]/nav').get_attribute("outerHTML")
    count_pages = cnt_pages.count('<a')
    print(count_pages)

    comp = []
    # count the number of companies on the page
    cnt= driver.find_element("xpath",'/html/body/div[1]/main/div/div[3]/div/div/div[1]/div/div[1]/ul').get_attribute("outerHTML")
    count1 = cnt.count('<li')

    for i in range(1,count1+1):

        
        job_role1=driver.find_element("xpath", f'//*[@id="job-list"]/li[{i}]/div/div[1]/h3/a').get_attribute("innerHTML")
        company_city=driver.find_element("xpath", f'//*[@id="job-list"]/li[{i}]/div/p[1]/span[2]').get_attribute("innerHTML")
        company_name=driver.find_element(By.XPATH,f'//*[@id="job-list"]/li[{i}]/div/p[1]/span[1]/span').get_attribute("innerHTML")
        job_description=driver.find_element(By.XPATH,f'//*[@id="job-list"]/li[{i}]/div/p[2]').get_attribute("innerHTML")
        # apply_url = driver.find_element(By.XPATH,f'/html/body/div[1]/main/div/div[3]/div/div/div[2]/div/aside/header/div/div/div[2]/div[2]/a')
        try:    
            job_salary = driver.find_element(By.XPATH,f'//*[@id="job-list"]/li[{i}]/div/div[2]/div/p').get_attribute("innerHTML")
            res = [int(s) for s in re.findall(r'\b\d+\b', job_salary)]
            print(res)
            ##### ADD JOB SALARY DATA API HERE ############
            mean_salary = mean(res)
        except:
            print('salary not available')
            job_salary='salary data not available'
            mean_salary = 0

        job_div=driver.find_element("xpath", f'/html/body/div[1]/main/div/div[3]/div/div/div[1]/div/div[1]/ul/li[{i}]/div')
        job_div.click()
        time.sleep(3)
        url_link=driver.find_element("xpath", f'/html/body/div[1]/main/div/div[3]/div/div/div[2]/div/aside/header/div/div/div[2]/div[2]/a').get_attribute("href")
        
        comp.append({'company_name':company_name,'job_role':job_role1,'company_city':company_city,'job_description':job_description,'job_salary':job_salary,'mean_salary':mean_salary,'job_url':url_link})

        # if j >1:
        #     j +=1
        for j in range(1,count_pages+1):
            next_page = driver.find_element('xpath', f'/html/body/div[1]/main/div/div[3]/div/div/div[1]/div/div[2]/div[1]/nav/a[{j}]').get_attribute('href')
            driver.get(next_page)
            print(j)
            # count the number of companies on the page
            cnt= driver.find_element("xpath",'/html/body/div[1]/main/div/div[3]/div/div/div[1]/div/div[1]/ul').get_attribute("outerHTML")
            count1 = cnt.count('<li')

            for i in range(1,count1+1):

                
                job_role1=driver.find_element("xpath", f'//*[@id="job-list"]/li[{i}]/div/div[1]/h3/a').get_attribute("innerHTML")
                company_city=driver.find_element("xpath", f'//*[@id="job-list"]/li[{i}]/div/p[1]/span[2]').get_attribute("innerHTML")
                company_name=driver.find_element(By.XPATH,f'//*[@id="job-list"]/li[{i}]/div/p[1]/span[1]/span').get_attribute("innerHTML")
                job_description=driver.find_element(By.XPATH,f'//*[@id="job-list"]/li[{i}]/div/p[2]').get_attribute("innerHTML")
                # apply_url = driver.find_element(By.XPATH,f'/html/body/div[1]/main/div/div[3]/div/div/div[2]/div/aside/header/div/div/div[2]/div[2]/a')
                try:    
                    job_salary = driver.find_element(By.XPATH,f'//*[@id="job-list"]/li[{i}]/div/div[2]/div/p').get_attribute("innerHTML")
                    res = [int(s) for s in re.findall(r'\b\d+\b', job_salary)]
                    print(res)
                    ##### ADD JOB SALARY DATA API HERE ############
                    mean_salary = mean(res)
                except:
                    print('salary not available')
                    job_salary='salary data not available'
                    mean_salary = 0

                job_div=driver.find_element("xpath", f'/html/body/div[1]/main/div/div[3]/div/div/div[1]/div/div[1]/ul/li[{i}]/div')
                job_div.click()
                time.sleep(3)
                url_link=driver.find_element("xpath", f'/html/body/div[1]/main/div/div[3]/div/div/div[2]/div/aside/header/div/div/div[2]/div[2]/a').get_attribute("href")
                
                comp.append({'company_name':company_name,'job_role':job_role1,'company_city':company_city,'job_description':job_description,'job_salary':job_salary,'mean_salary':mean_salary,'job_url':url_link})
            driver.back()
            time.sleep(3)

    # store all the details in a JSON
    with open("company_details.json", 'w') as myfile:
        myfile.write(json.dumps(comp,indent = 4))

    return None

company_data('data engineer','san diego')