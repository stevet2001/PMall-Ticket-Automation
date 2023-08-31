from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import getpass

#####ACCESSING PMALL ADMIN#####
driver = webdriver.Chrome()

driver.get("https://www.pmalladmin.com/")

#driver.get("C:/Users/SThomas/Desktop/password_template.html")

username_input = input('Enter your username: ')
password_input = getpass.getpass('Enter your password: ')

username = driver.find_element(By.NAME, 'loginname')
password = driver.find_element(By.NAME, 'passwd')

username.send_keys(username_input)
password.send_keys(password_input)
password.send_keys(Keys.RETURN)

button = driver.find_element(By.NAME, 'aButton')
button.click()

#####LOCATING IT REQUESTS TABLE#####
frame = driver.find_element(By.NAME, 'PMALLMAIN' )
driver.switch_to.frame(frame)
table_element = driver.find_element(By.XPATH, '/html/body/table')
table_rows = table_element.find_elements(By.TAG_NAME, 'tr')

#####STORING DATA IN AN ARRAY####
table_data = []
for row in table_rows:
    row_data = []
    columns = row.find_elements(By.TAG_NAME, 'td')
    for column in columns:
        row_data.append(column.text)
    table_data.append(row_data)

####CHECKING WHETHER OR NOT 'PASSWORD' IS FOUND####
for row_index, row in enumerate(table_data):
    for col_index, element in enumerate(row):
        if 'password' in element.lower():  # Using .lower() to make the search case-insensitive
            print(f"'password' found at row {row_index}, column {col_index}")
            
            # Add your specific action here

#If 'password' was not found in the entire array
else:
    print("'password' not found in the table")

time.sleep(50)
driver.close()
