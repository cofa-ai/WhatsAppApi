from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from time import sleep


class WhatsApp:
    driver = webdriver.Firefox()
    driver.get("https://web.whatsapp.com")

    def wait_for_auth(self):
        try:
            qr = self.get_qr_element()
            qr_code_id = ''
            qr_count = 0
            while True:
                current_qr_code_id = qr.get_attribute('data-ref')
                if self.need_to_refresh():
                    qr.click()
                    qr = self.get_qr_element()
                if current_qr_code_id != qr_code_id:
                    qr_code_id = current_qr_code_id
                    qr.screenshot('qr.png')
                    qr_count += 1
                sleep(2)
        except (StaleElementReferenceException, TimeoutException):
            if self.is_authentithicated():
                return True
            self.wait_for_auth()

    def get_qr_element(self):
        qr = WebDriverWait(self.driver, 10).until(
                lambda x: x.find_element_by_css_selector("div[data-ref]")
                )
        return qr

    def need_to_refresh(self):
        try:
            self.driver.find_element_by_xpath("//span[@data-testid='refresh-large']")
            return True
        except NoSuchElementException:
            return False

    def is_authentithicated(self):
        try:
            x = self.driver.find_element_by_xpath("//span[@data-icon='chat']")
            return True
        except NoSuchElementException:
            return False


if __name__ == '__main__':
    wa = WhatsApp()
    wa.wait_for_auth()
    wa.driver.close()
