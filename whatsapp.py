from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class WhatsApp:
    driver = webdriver.Firefox()

    def get_qr_code(self):
        self.driver.get("https://web.whatsapp.com")
        qr = WebDriverWait(self.driver, 10).until(
                lambda x: x.find_element_by_css_selector("div[data-ref]")
                )
        qr.screenshot('qr.png')


if __name__ == '__main__':
    wa = WhatsApp()
    wa.get_qr_code()
