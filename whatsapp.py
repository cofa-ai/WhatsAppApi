from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


class WhatsApp:
    driver = webdriver.Firefox()

    def wait_for_auth(self):
        qr = self.get_qr_element()
        qr_code_id = qr.get_attribute('data-ref')
        qr_count = 1
        while True:
            current_qr_code_id = qr.get_attribute('data-ref')
            print(current_qr_code_id)
            if current_qr_code_id != qr_code_id:
                qr_code_id = current_qr_code_id
                qr.screenshot('qr.png')
                qr_count += 1
                print(qr_count)
            sleep(2)

    def get_qr_element(self):
        self.driver.get("https://web.whatsapp.com")
        qr = WebDriverWait(self.driver, 10).until(
                lambda x: x.find_element_by_css_selector("div[data-ref]")
                )
        return qr


if __name__ == '__main__':
    wa = WhatsApp()
    wa.wait_for_auth()
