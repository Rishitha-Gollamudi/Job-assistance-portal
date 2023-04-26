

# import all the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #error handling
from selenium.common.exceptions import TimeoutException #timeout if not found
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
# initialise chrome driver
import json
import time
option = Options()

option.add_argument("--headless")


class questions:
    def questions(job,loc):
        company_questions=[]
        y='https://www.glassdoor.com/Interview/index.htm'
        driver = webdriver.Chrome('C:\\chromedriver.exe')
        driver.get(y)
        print(driver)
        driver.set_window_size(1920, 1080)
        wait = WebDriverWait(driver, 250)
        

        inputElement = driver.find_element(By.NAME, "typedKeyword")


        inputElement.send_keys(f'{job}')
        time.sleep(3)
        
        
        inputElement.send_keys(Keys.ENTER)
        time.sleep(3)
        # inputElement1 = driver.find_element(By.XPATH, "/html/body/header/nav/div/div/div/div[4]/div[2]/form/div/div[2]/div/div/div/div/input")
        # lst = []
        # for i in range(2,6):
        #     time.sleep(2)
        #     lst.append(driver.find_element(By.XPATH,f'/html/body/div[3]/div/div/div/div/div/div/div[2]/article/div[8]/div/div/div/div/div[2]/div[1]/div[2]/div[3]/div[2]/div/div[1]/ul/li[4]/a').get_attribute('href'))
        #     time.sleep(3)
        # print(lst)
        # inputElement1.send_keys(f'{loc}')
    #     for j in range(5):   
        for i in range(1,11):

            try:
                questions=driver.find_element(By.XPATH,f'//*[@id="BaseLayout"]/div/div[2]/div[1]/div[2]/div[2]/div[{i}]/div/div/div[2]/h3').get_attribute("innerHTML")
                company=driver.find_element(By.XPATH,f'//*[@id="BaseLayout"]/div/div[2]/div[1]/div[2]/div[2]/div[{i}]/div/a/img').get_attribute("alt")
                company_questions.append({'questions':questions,'Company':company})
            except:
                print("No element error occurred")
        if len(company_questions)==0:
            company_questions.append({'questions':'No questions available','Company':'No company available'})

            



        
    #     # store all the details in a JSON 
        with open("static/company_questions.json", 'w') as myfile:
            myfile.write(json.dumps(company_questions,indent = 4))

        return company_questions

    # questions('software engineer','Austin, TX')