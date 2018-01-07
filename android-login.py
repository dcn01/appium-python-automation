import os
import unittest
import time


from appium import webdriver


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AndroidLogin(unittest.TestCase):
    def setUp(self):

        desired_caps = {
        'platformName': 'Android',
        'platformVersion': '7.0',
        'deviceName': 'Android Emulator',
        'app': PATH('android-debug.apk'),
        'newCommandTimeout': 240
    }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_customer_login(self):
        

#        print(self.driver.contexts)
#        print(self.driver.contexts[0])
#        print(self.driver.contexts[1])

        self.driver.switch_to.context('WEBVIEW_com.tidy.clientmobile')

        LoginButton = self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-introduction > ion-content > div.scroll-content > button > span")
        LoginButton.click()
#        print(LoginButton)

        emailField = self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-login > ion-content > div.scroll-content > div > form > ion-item:nth-child(1) > div.item-inner > div > ion-input > input")
        emailField.send_keys("helivelton@test1000.com")

        passwdField = self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-login > ion-content > div.scroll-content > div > form > ion-item:nth-child(3) > div.item-inner > div > ion-input > input")
        passwdField.send_keys("12345678")

        self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-login > ion-content > div.scroll-content > div > form > button.disable-hover.button.button-md.button-default.button-default-md.button-block.button-block-md.button-md-tidy_green > span").click()

        time.sleep(10)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)
