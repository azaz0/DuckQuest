import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class QuestForm:

    def __init__(self, start_value: 0, end_value: 100):
        self.start_value = start_value
        self.end_value = end_value
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self):
        self.driver.get("https://techsummer.ringieraxelspringer.com/recruitmentTask")

    def close_notification(self):
        notification_button = '/html/body/div[2]/div[1]/div[2]/div/div[6]/button[2]'
        self.use_clickable_element(notification_button)

    def sad_duck_close(self):
        close_button = '/html[1]/body[1]/div[1]/div[1]/span[1]'
        self.use_clickable_element(close_button)

    def solve_quest(self, n):
        answer_input = self.driver.find_element(By.XPATH,
                                                '/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[2]/input[1]')
        answer_input.clear()
        answer_input.send_keys(str(n))
        submit_button = '/html[1]/body[1]/main[1]/div[1]/div[1]/div[1]/div[3]/div[1]'
        self.use_clickable_element(submit_button)

    def make_screenshot(self, n):
        screenshot_filename = f'screenshots/ss_{n}.png'
        self.driver.save_screenshot(screenshot_filename)

    def use_clickable_element(self, element_xpath):
        element = self.wait.until(EC.visibility_of_element_located((By.XPATH, element_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    def close_browser(self):
        self.driver.quit()

    def start_task(self):
        self.close_notification()
        for n in range(self.start_value, self.end_value + 1):
            self.solve_quest(n)
            self.make_screenshot(n)
            self.sad_duck_close()


if __name__ == "__main__":
    quest_form_test = QuestForm(0, 100)
    quest_form_test.open_page()
    quest_form_test.start_task()
    quest_form_test.close_browser()
