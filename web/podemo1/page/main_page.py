import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web.podemo1.page.add_member_page import AddMemberPage
from web.podemo1.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self):
    #     options = Options()
    #     options.debugger_address = '127.0.0.1:9222'
    #     self.driver = webdriver.Chrome(options=options)
    #     self.driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    base_url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_addmenber(self):
        # 直接在首页添加联系人
        # self.driver.find_element(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return AddMemberPage(self.driver)

    def goto_contacts(self):
        time.sleep(5)
        # 点击 【通讯录】

        self.find(By.ID, 'menu_contacts').click()
        time.sleep(5)

        # 点击 【添加联系人】按钮
        # self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()

        # 显示等待
        locator = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')

        # 封装一个方法
        # element:WebElement = WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        # element = self.wait_for_click(locator)
        # element.click()

        def wait_for_next(x: WebDriver):
            try:
                x.find_element(*locator).click()
                return x.find_element(By.ID, 'username')
            except:
                return False

        WebDriverWait(self.driver, 10).until(wait_for_next)

        return AddMemberPage(self.driver)
