import os
import unittest
import time
import appium
import desired_capabilities_android


from appium import webdriver


class AndroidSignup(unittest.TestCase):
    def setUp(self):

        desired_caps = desired_capabilities_android.get_desired_capabilities()
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_customer_signup(self):

        customer_number = 14
        
        self.driver.switch_to.context('WEBVIEW_com.tidy.clientmobile')

        time.sleep(2)
        #click signup button
        self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-introduction > ion-content > div.scroll-content > div > button:nth-child(1) > span").click()

        #first name
        first_name = self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-sign-up > ion-content > div.scroll-content > div > form > ion-item:nth-child(1) > div.item-inner > div > ion-input > input")        
        first_name.send_keys("heliveltonPython" + str(customer_number))

        #last name
        last_name = self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-sign-up > ion-content > div.scroll-content > div > form > ion-item:nth-child(3) > div.item-inner > div > ion-input > input")
        last_name.send_keys("testPyhon" + str(customer_number))

        #email
        email_field = self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-sign-up > ion-content > div.scroll-content > div > form > ion-item:nth-child(5) > div.item-inner > div > ion-input > input")
        email_field.send_keys("helivelton@testpython"+ str(customer_number) +".com")

        #password
        passwd_field = self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-sign-up > ion-content > div.scroll-content > div > form > ion-item:nth-child(7) > div.item-inner > div > ion-input > input")
        passwd_field.send_keys("12345678")

        #click continue
        self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-sign-up > ion-content > div.scroll-content > div > form > button > span").click()

        time.sleep(5)

        #address
        address_field = self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-address > ion-content > div.scroll-content > div > form > ion-item.item.item-block.item-md.item-label-stacked.item-input.ng-untouched.ng-pristine.ng-invalid.item-multiple-inputs > div.item-inner > div > ion-input:nth-child(2) > input")
        address_field.send_keys("105 us 89 browning")

        time.sleep(5)

        #click address dropdown
        self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-address > ion-content > div.scroll-content > div > form > ion-list > ion-item > div.item-inner > div > ion-label").click()

        #address2
        address_field2 = self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-address > ion-content > div.scroll-content > div > form > ion-item:nth-child(5) > div.item-inner > div > ion-input > input")
        address_field2.send_keys("suite 2")


        time.sleep(3)
        #click View Pricing & Availability
        self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-address > ion-content > div.scroll-content > div > form > tidy-active-button > button > span").click()

        time.sleep(3)
        #select tidy 1 hour
        self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-plan > ion-content > div.scroll-content > div > div.section-plan > ion-row.cleaning-type-options.row > ion-col:nth-child(1) > label > span").click()

        #select last frequency
        self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-plan > ion-content > div.scroll-content > div > ion-row.plan-frequency.row > ion-col:nth-child(3) > label > span").click()

        time.sleep(3)
        #select time slot
        self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-plan > ion-content > div.scroll-content > div > div:nth-child(6) > ion-row > ion-col:nth-child(1) > label > span").click()

        #click Next button
        self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-plan > ion-content > div.scroll-content > div > ion-row:nth-child(7) > ion-col > button > span").click()

        time.sleep(3)

        #cc number
        cc_number = self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-confirm > ion-content > div.scroll-content > div > form > ion-row:nth-child(1) > ion-col > ion-item > div.item-inner > div > ion-input > input")
        cc_number.send_keys("5555555555554444")

        #cc expiration
        cc_expiration = self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-confirm > ion-content > div.scroll-content > div > form > ion-row:nth-child(2) > ion-col:nth-child(1) > ion-item > div.item-inner > div > ion-input > input")
        cc_expiration.send_keys("1120")

        #cc CVC
        cc_cvc = self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-confirm > ion-content > div.scroll-content > div > form > ion-row:nth-child(2) > ion-col:nth-child(2) > ion-item > div.item-inner > div > ion-input > input")
        cc_cvc.send_keys("123")

        #click Book now
        self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-confirm > ion-content > div.scroll-content > div > form > button > span").click()

        time.sleep(20)
        #cell phone                                            
        cell_phone = self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-contact > ion-content > div.scroll-content > div > form > ion-item:nth-child(1) > div.item-inner > div > ion-input > input")
#        cell_phone = self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-contact > ion-content > div.scroll-content > div > form > ion-item.item.item-block.item-md.item-label-stacked.item-input.ng-pristine.ng-invalid.ng-touched > div.item-inner > div > ion-input > input")
        cell_phone.send_keys("1111111111")

        #How to Park
        how_to_park = self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-contact > ion-content > div.scroll-content > div > form > ion-item.item.item-block.item-md.item-label-stacked.item-textarea.item-input.ng-untouched.ng-pristine.ng-invalid > div.item-inner > div > ion-textarea > textarea")
        how_to_park.send_keys("parking instructions")

        #How to Lock
        how_to_lock = self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-contact > ion-content > div.scroll-content > div > form > ion-item.item.item-block.item-md.item-label-stacked.item-textarea.item-input.ng-untouched.ng-pristine.ng-valid > div.item-inner > div > ion-textarea > textarea")
        how_to_lock.send_keys("locking instructions")

        #click Next button
        self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-contact > ion-content > div.scroll-content > div > form > button > span").click()

        time.sleep(3)
        #click Next button
        self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-backup-time > ion-content > div.scroll-content > div > form > button > span").click()

        time.sleep(3)
        #click Use Most Popular To Dos
        self.driver.find_element_by_css_selector("body > ion-app > ng-component > ion-split-pane > ion-nav > page-my-house > ion-content > div.scroll-content > div > form > button:nth-child(4) > span").click()

        time.sleep(10)




if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidSignup)
    unittest.TextTestRunner(verbosity=2).run(suite)
