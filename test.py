import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from selenium import webdriver
from selenium.webdriver.common.by import By

class ChromeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_eight_components(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/registro")

        title = driver.title
        assert title == "Registrate"
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://127.0.0.1:5000/registro")
        elem = driver.find_element('name')
        elem.send_keys("Joel")
        elem = driver.find_element('apellidos')
        elem.send_keys("Castillon")
        elem = driver.find_element('email')
        elem.send_keys("levi@gmai.com")
        elem = driver.find_element('password')
        elem.send_keys("levvvv")
        elem.send_keys(Keys.RETURN)
        assert "http://127.0.0.1:5000/home" == driver.current_url
        driver.quit()

if __name__ == "__main__":
    unittest.main()