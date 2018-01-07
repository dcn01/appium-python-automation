#!/usr/bin/env python

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os
import unittest
import time


from appium import webdriver


PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AndroidLogin(unittest.TestCase):
    def setUp(self):
#        desired_caps = desired_capabilities.get_desired_capabilities('android-debug.apk')
        desired_caps = {
        'platformName': 'Android',
        'platformVersion': '7.0',
        'deviceName': 'Android Emulator',
        'app': PATH('android-debug.apk'),
        'newCommandTimeout': 240
    }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#        abs_path =  os.path.abspath('../../apps/android-debug.apk')
#        self.driver = webdriver.Remote(
#            command_executor='http://127.0.0.1:4723/wd/hub',
#            desired_capabilities={
##              'app': os.path.abspath(abs_path),
 ###             'platformName': 'Android',
###              'deviceName': 'Android Emulator',
#              'autoWebview': 'true',
#              'automationName': 'selendroid'
#        })

    def tearDown(self):
        self.driver.quit()

    def test_find_single_element(self):
        
        self.driver.implicitly_wait(10)
        webview = self.driver.contexts[0]

        print(self.driver.contexts)
        print(self.driver.contexts[0])
        print(self.driver.contexts[1])
        self.driver.switch_to.context('WEBVIEW_com.tidy.clientmobile')
#        webview = self.driver.contexts.last
#        self.driver._switch_to.context(webview)
        self.driver.implicitly_wait(10)
        elements = self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-introduction > ion-content > div.scroll-content > button > span")
        elements.click()
        print(elements)

        emailField = self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-login > ion-content > div.scroll-content > div > form > ion-item:nth-child(1) > div.item-inner > div > ion-input > input")
        emailField.send_keys("helivelton@test1000.com")

        passwdField = self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-login > ion-content > div.scroll-content > div > form > ion-item:nth-child(3) > div.item-inner > div > ion-input > input")
        passwdField.send_keys("12345678")

        self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-login > ion-content > div.scroll-content > div > form > button.disable-hover.button.button-md.button-default.button-default-md.button-block.button-block-md.button-md-tidy_green > span").click()

        time.sleep(10)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidLogin)
    unittest.TextTestRunner(verbosity=2).run(suite)
