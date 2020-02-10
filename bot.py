from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


class LinkedInBot():
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

        # Login process
        # fill username, password and click enter.
        self.driver.find_element_by_xpath("//*[@id='username']").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='password']").send_keys(password, Keys.RETURN)

        # go to 'my-network' tab
        self.driver.find_element_by_xpath("//*[@id='mynetwork-nav-item']/a").click()

        sleep(2)
        print("bot opened my network")

        for button in self.driver.find_elements_by_xpath("//button[@data-control-name='people_connect']"):
            button.click()
            button.send_keys(Keys.ARROW_DOWN)
            button.send_keys(Keys.ARROW_DOWN)

        sleep(2)
        print("bot ended")


LinkedInBot("email", "password")
