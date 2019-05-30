import pytest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import requests
from PIL import Image
from io import BytesIO
import os
import logging
import ctypes

user32 = ctypes.windll.user32


class TestYandex:

    def setup(self):
        self.driver = webdriver.Chrome('chromedriver')
        self.driver.set_window_size(1600, 1024)
        self.driver.implicitly_wait(10)
        self.driver.get('https://yandex.ru/')

    def test_yandex_search(self):
        search_word = 'Тензор'

        driver = self.driver
        wait = WebDriverWait(driver, 5)

        try: # проверяем наличие поля поиска
            logging.info('проверяем наличие поля поиска')
            search_field = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="input__box"]/input[@id="text"]')))
        except TimeoutException:
            logging.error('поле поиска отсутствует')
            raise
        search_field.send_keys(search_word)

        try: # проверяем, появилась таблица с подсказками (suggest) или нет
            logging.info('проверяем, появилась таблица с подсказками (suggest) или нет')
            wait.until(EC.visibility_of_element_located((By.XPATH, '//div[@class="popup__content"]')))
        except TimeoutException:
            logging.error('таблица с подсказками (suggest) не появилась')
            raise

        search_field.send_keys(Keys.ENTER)
        first_link = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[@role="main"]/li[1]/div[1]/h2/a')))
        first_link.click()
        driver.switch_to.window(window_name=self.driver.window_handles[1]) # меняем вкладку браузера

        try: # проверяем приведет первая ссылка поиска на https://tensor.ru/ или нет
            logging.info('проверяем приведет первая ссылка поиска на https://tensor.ru/ или нет')
            assert driver.current_url == 'https://tensor.ru/', \
                'адрес "https://tensor.ru/" не является перым результатом поиска по запросу "{}"'.format(search_word)
        except AssertionError as e:
            logging.error(e)
            raise

    def test_yandex_picture_search(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)

        try: # проверяем наличие ссылки «Картинки» на странице
            logging.info('проверяем наличие ссылки «Картинки» на странице')
            link_images = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="home-arrow__tabs"]/div/a[@data-id="images"]')))
        except TimeoutException:
            logging.error('ссылки «Картинки» отсутствует на странице')
            raise
        link_images.click()

        try: # проверяем, что полученная страница https://yandex.ru/images/
            logging.info('проверяем, что полученная страница https://yandex.ru/images/')
            assert driver.current_url == 'https://yandex.ru/images/', 'текущая траница не соответствует целевой'
        except AssertionError as e:
            logging.error(e)
            raise

        first_image = driver.find_element_by_class_name('cl-teaser__link')
        first_image.click()
        first_image_link = self.get_img_link(wait)
        self.check_img(first_image_link)
        self.chech_navigation_button(wait, '//div[@title="Следующая"]').click()
        second_image_link = self.get_img_link(wait)
        self.check_img(second_image_link)
        self.chech_navigation_button(wait, '//div[@title="Предыдущая"]').click()
        prev_img_link = self.get_img_link(wait)
        try: # проверяем совпадают или нет ссылки на изображения
            logging.info('проверяем совпадают или нет ссылки на изображения')
            assert prev_img_link == first_image_link, 'ссылки на изображения не совпадают'
        except AssertionError as e:
            logging.error(e)
            raise

    def get_img_link(self, wait):
        xpath = r'//div[@class="image__wrap__i"]/img[@data-il="image__wrap"]'
        try: # получаем ссылку на картинку
            logging.info('получаем ссылку на картинку')
            return wait.until(EC.presence_of_element_located((By.XPATH, xpath))).get_attribute('src')
        except TimeoutException:
            logging.error('елемент {} не найден'.format(xpath))
            raise

    def chech_navigation_button(self, wait, xpath):
        try: # проверяем виден или нет елемент навигации '>'
            logging.info('проверяем виден или нет елемент навигации ">" ')
            next_image = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            return next_image
        except TimeoutException:
            logging.error('элемент навигации {} не найден'.format(xpath))
            raise

    def check_img(self, url):
        try: # проверяем, что картинка существует
            logging.info('проверяем, что изображение существует по указанной ссылке')
            assert Image.open(BytesIO(requests.get(url).content)), 'изображение {} не найдено'.format(url)
        except AssertionError as e:
            logging.error(e)
            raise

    def teardown(self):
        self.driver.quit()


if __name__ == '__main__':
    pytest.main(args=['-sv', os.path.abspath(__file__)])