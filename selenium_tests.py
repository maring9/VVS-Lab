from selenium import webdriver
from selenium.webdriver.chrome.options import Options


CHROMEDRIVER_PATH = '/home/coreai/Desktop/VVS/chromedriver_linux64/chromedriver'


def create_webdriver(CHROMEDRIVER_PATH):
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                              chrome_options=chrome_options)
    return driver


def test_button_exists():
    chrome_driver = create_webdriver(CHROMEDRIVER_PATH)
    chrome_driver.get('http://localhost:8080')
    next_page_button = chrome_driver.find_element_by_xpath('/html/body/a')
    assert next_page_button is not None
    

def test_next_page_button():
    chrome_driver = create_webdriver(CHROMEDRIVER_PATH)
    chrome_driver.get('http://localhost:8080')
    next_page_button = chrome_driver.find_element_by_xpath('/html/body/a')
    next_page_button.click()
    assert chrome_driver.current_url == 'http://localhost:8080/page.html'
    

if __name__ == '__main__':
    test_button_exists()
    test_next_page_button()
    
    print('Test successful')