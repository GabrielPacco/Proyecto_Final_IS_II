import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome import service as ChromeService
import time

class test_login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

    def test_login(self):
        driver = self.driver

        driver.get("http://127.0.0.1:5000/")

        # Comprobar title
        title : driver.title
        self.assertIn("Sistema de Publicación de Eventos", driver.title)

        # implicit wait
        driver.implicitly_wait(10)

        # Maximize the browser
        driver.maximize_window()

        # Click on Math Calculators
        math_calc = driver.find_element(by=By.XPATH, value="//*[@id='navbarResponsive']/ul/li[2]/a")
        math_calc.click()
        
        driver.implicitly_wait(10)

        # Enter value 10 in the first number of the percent Calculator
        first_text = driver.find_element(by=By.XPATH, value="//*[@id='typeEmailX']")
        
        first_text.send_keys("LeviC@gmail.com")
        # Enter value 50 in the second number of the percent Calculator

        second_text = driver.find_element(by=By.XPATH, value="//*[@id='typePasswordX']")
        second_text.send_keys("Levi")

        #Click Calculate Button
        button = driver.find_element(by=By.XPATH, value="//*[@id='content']/input")
        button.click()
        
        # implicit wait
        driver.implicitly_wait(10)
        
        #Print a Log In message to the screen
        print(f"\n Ingreso exitoso")

    def tearDown(self):
        # Close the Browser.
        self.driver.close()

if __name__ == "__main__":
    unittest.main()