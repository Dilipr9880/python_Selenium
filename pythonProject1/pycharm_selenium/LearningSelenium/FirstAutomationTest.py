from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Use raw string for the path
chrome_service = Service(r"D:\pycharm\pythonProject1\chromedriver.exe")

# Initialize the Chrome driver with the service
driver = webdriver.Chrome(service=chrome_service)

driver.get("https://www.youtube.com")
print(driver.title)
driver.maximize_window()
driver.close()