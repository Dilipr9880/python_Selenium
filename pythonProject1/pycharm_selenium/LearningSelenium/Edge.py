from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Use raw string for the path
edge_service = Service(r"C:\Users\CSC\Downloads\edgedriver_win64\msedgedriver.exe")

# Initialize the Chrome driver with the service
driver = webdriver.Edge(service=edge_service)

driver.get("https://www.youtube.com")
print(driver.title)
driver.maximize_window()
driver.close()