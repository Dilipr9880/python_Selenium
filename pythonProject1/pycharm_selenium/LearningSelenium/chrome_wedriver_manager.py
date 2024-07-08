from selenium import webdriver
from webdriver_manager import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.youtube.com")
driver.maximize_window()
print(driver.title)
driver.close()