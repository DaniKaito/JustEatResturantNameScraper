import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time


def main():
	createOutput()
	driver = setup()
	url = "Insert url to scrape: "
	driver.get(url)

	#SCROLLING DOWN TO THE BOTTOM FUNCION
	SCROLL_PAUSE_TIME = 0.5
	last_height = driver.execute_script("return document.body.scrollHeight")

	while True:
	    # Scroll down to bottom
	    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

	    # Wait to load page
	    time.sleep(SCROLL_PAUSE_TIME)

	    # Calculate new scroll height and compare with last scroll height
	    new_height = driver.execute_script("return document.body.scrollHeight")
	    if new_height == last_height:
	        break
	    last_height = new_height

	#get all titles
	rows = driver.find_elements(By.CLASS_NAME, 'RestaurantCard_c-restaurantCard-name_1Zwfd')
	print(f"Found a total of {len(rows)} resturants in the area")
	for row in rows:
		with open("output.txt", "a", encoding="utf8") as f:
			f.write(row.text)
			f.write("\n")
			print(f"wrote the following title: {row.text}")

#create output file
def createOutput():
	with open("output.txt", "w") as f:
		print("created output txt file")

#return driver in headless mode
def setup(headless=True):
	options = uc.ChromeOptions()
	options.headless = headless
	return uc.Chrome(options=options)

main()