from selenium import webdriver
from pandas import read_html
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get('https://www.techlistic.com/2017/02/automate-demo-web-table-with-selenium.html')

table_element = driver.find_element(By.ID, 'customers')  
rows = table_element.find_elements(By.TAG_NAME, 'tr')  

for row in rows:
    
    cells = row.find_elements(By.TAG_NAME, 'td')  

    
    for cell in cells:
        data = cell.text  
        print(data)  # 


df = read_html(driver.page_source)[0]  
driver.quit()
