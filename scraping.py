from selenium import webdriver
import schedule
import time

chrome_path = "chromedriver.exe"

def scrape_cards_count():
	driver_options = webdriver.ChromeOptions()
	driver_options.add_argument('--ignore-certificate-errors')
	driver_options.add_argument('--incognito')
	driver_options.add_argument('--headless')
	driver = webdriver.Chrome(chrome_path, chrome_options = driver_options)
	try:
		driver.get("https://jsonplaceholder.typicode.com/")
		message = driver.find_element_by_id("run-button")
		print("Cards count: ", message.text)
	except:
		print("Error")
	driver.close()
	
schedule.every(5).seconds.do(scrape_cards_count)

while 1:
	schedule.run_pending()
	time.sleep(5)
