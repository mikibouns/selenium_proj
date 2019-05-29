from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class SeleniumTestSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.implicitly_wait(5)
        self.driver.get('https://yandex.ru/')

    # def test_yandex_search(self):
    #     driver = self.driver
    #     search_field = driver.find_element_by_xpath('//span[@class="input__box"]/input[@id="text"]')
    #     assert search_field
    #     search_field.send_keys('Тензор')
    #     assert driver.find_element_by_class_name('popup_visibility_visible')
    #     search_field.send_keys(Keys.ENTER)
    #     result = driver.find_element_by_xpath('//div[@class="content__left"]/ul/li[1]/div/h2/a')
    #     expected_result = driver.find_element_by_link_text('tensor.ru')
    #     self.assertEqual(result.get_attribute('href'),
    #                      expected_result.get_attribute('href'),
    #                      'htttps://tensor.ru/ не перваz ссылка в поисковой системе "Яндекс" по запросу "Тензор"')
    #     expected_result.click()

    def test_yandex_picture_search(self):
        driver = self.driver
        images_link = driver.find_element_by_xpath('//div[@class="home-arrow__tabs"]/div/a[@data-id="images"]')
        assert images_link
        images_link.click()
        first_img = driver.find_element_by_class_name('cl-teaser__link')
        first_img.click()
        assert driver.find_element_by_class_name('wrap__inner_layout')
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    run = unittest.main()
    print(run)