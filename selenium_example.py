from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from settings import webpage

# options = Options()
# options.headless = True

driver = webdriver.Firefox(
    # options=options, 
    executable_path = "/home/steadylearner/geckodriver"
)

driver.get(webpage)

print(driver.title)
target = driver.find_element_by_xpath('//button[@aria-label="Like"]')

for i in range(0, 100):
    target.click()


