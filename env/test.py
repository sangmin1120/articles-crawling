from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urllib import request        
import time
from datetime import datetime

search=input('원하는 검색어 입력: ')
print(search+' 상위 5개 기사 출력')
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get("http://www.naver.com")

time.sleep(2)

elem=driver.find_element("name",'query')
elem.send_keys(search)
elem.submit()

time.sleep(2)

page=driver.find_element(By.XPATH,'//*[@id="lnb"]/div[1]/div/ul/li[2]/a')
page.click()

news=driver.find_elements(By.CLASS_NAME,'news_tit')
f=open("articles.txt",'a')
f.write(datetime.today().strftime('%Y-%m-%d'))
f.write(search+'관련 기사\n')

count=0
for i in news:
    title=i.text
    f.write(str(count+1)+title)
    count+=1
    if count>5:
        break


f.close()   
time.sleep(5)


# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.clo