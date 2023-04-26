####### mailID: SI507test@gmail.com Password: SI507project


# import all the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #error handling
from selenium.common.exceptions import TimeoutException #timeout if not found
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
# initialise chrome driver
import json
import time
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = r"C:\chromedriver.exe"
# op = webdriver.ChromeOptions()
# op.add_argument('headless')


class Reviews:

    def company_reviews(company):
        y=f'https://www.glassdoor.com/Search/results.htm?keyword={company}'
        driver = webdriver.Chrome('C:\\chromedriver.exe')
        # driver = webdriver.Chrome(options=op)
        driver.get(y)
        company_reviews_list=[]
        driver.set_window_size(1920, 1080)
        wait = WebDriverWait(driver, 250)


        # inputElement = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/div/div/div/div[1]/div/input")
        # inputElement.send_keys('Tesla')
        # inputElement = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div/div[2]/button")
        # inputElement.send_keys(Keys.ENTER)

        inputElement = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div[1]/div[1]/a[1]")
        inputElement.send_keys(Keys.ENTER)
        time.sleep(2)
        inputElement = driver.find_element(By.XPATH,"//*[@id='EmpLinksWrapper']/div[2]/div/div[1]/a[1]")
        inputElement.send_keys(Keys.ENTER)
        time.sleep(5)
        t = driver.find_element(By.CLASS_NAME,'hardsellContainer').is_displayed()
        if (t):
        
        # inputElement = driver.find_element(By.XPATH,"//*[@id='EmpLinksWrapper']/div[2]/div/div[1]/a[2]")
        # inputElement.send_keys(Keys.ENTER)

            inputElement = driver.find_element(By.NAME, "username")


            inputElement.send_keys('SI507test@gmail.com')
            inputElement.send_keys(Keys.ENTER)
            time.sleep(5)
            inputElement2 = driver.find_element(By.NAME, "password")
            inputElement2.send_keys('SI507project')
            inputElement2.send_keys(Keys.ENTER)

            time.sleep(5)
        cnt= int(driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/a[1]/div').get_attribute("innerHTML"))
        # count1 = cnt.count('<li')
        time.sleep(5)
        print(cnt)
        if cnt<10:
            for i in range(1,cnt+1):

                pros=driver.find_element(By.XPATH,f'/html/body/div[3]/div[1]/div[2]/main/div[6]/div/ol/li[{i}]/div/div/div[2]/div/div[2]/div[1]/p[2]').get_attribute("innerHTML")
                cons=driver.find_element(By.XPATH,f'/html/body/div[3]/div[1]/div[2]/main/div[6]/div/ol/li[{i}]/div/div/div[2]/div/div[2]/div[2]/p[2]').get_attribute("innerHTML")
                
                company_reviews_list.append({'pros':pros,'cons':cons})
            
        else:
            for j in range(1,5):
                
                for i in range(1,10+1):

                    pros=driver.find_element(By.XPATH,f'/html/body/div[3]/div[1]/div[2]/main/div[6]/div/ol/li[{i}]/div/div/div[2]/div/div[2]/div[1]/p[2]').get_attribute("innerHTML")
                    cons=driver.find_element(By.XPATH,f'/html/body/div[3]/div[1]/div[2]/main/div[6]/div/ol/li[{i}]/div/div/div[2]/div/div[2]/div[2]/p[2]').get_attribute("innerHTML")
                    
                    company_reviews_list.append({'pros':pros,'cons':cons})

                ele=driver.find_element(By.XPATH,'/html/body/div[3]/div[1]/div[2]/main/div[4]/div/div[1]/button[2]/span/svg')
                ele.click()

        driver.quit() 
        # store all the details in a JSON
        with open("company_reviews.json", 'w') as myfile:
            myfile.write(json.dumps(company_reviews_list,indent = 4))

        return company_reviews_list

    company_reviews('Zoox')