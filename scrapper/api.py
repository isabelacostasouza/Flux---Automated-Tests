import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class FluxTester():
    def __init__(self):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="./chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(100)
        return
    
    def login_on_dev(self, username, password):
        self.driver.get('http://inmetro.luar.dcc.ufmg.br/')

        username_element = self.driver.find_element_by_id("loginForm:login")
        username_element.send_keys(username)

        password_element = self.driver.find_element_by_id("loginForm:password")
        password_element.send_keys(password)
        
        login_button = self.driver.find_element_by_id("loginForm:j_id_t")
        login_button.click()

    def select_workflow(self, workflow_name):
        self.driver.get('http://inmetro.luar.dcc.ufmg.br/workflowSelection')

        for element in self.driver.find_elements_by_xpath('.//span[@class = "ui-panel-title"]'):
            if(workflow_name in element.text):
                element.find_element_by_xpath("../../..").click()
                return

    def create_instance(self):
        create_instance_buttton = self.driver.find_element_by_id('j_id_4g:instanceSelectionForm:j_id_4u')
        create_instance_buttton.click()

    def select_first_radiobox_option(self, radiobox_id):
        radiobox_options = self.driver.find_element_by_id(radiobox_id).find_elements_by_tag_name('tr')[0].find_element_by_tag_name('div')
        radiobox_options.location_once_scrolled_into_view
        self.time_sleep(1)
        radiobox_options.click()

    def select_first_register_option(self, dropdown_button_id, dropdown_list_id):
        self.time_sleep(0.5)
        self.blank_click()
        dropdown_button = self.driver.find_element_by_id(dropdown_button_id).find_element_by_tag_name('button')
        dropdown_button.location_once_scrolled_into_view
        self.time_sleep(0.5)
        dropdown_button.click()

        dropdown_list = self.driver.find_element_by_id(dropdown_list_id)
        dropdown_list.location_once_scrolled_into_view
        dropdown_list.click()

        self.blank_click()

    def select_first_dropdown_option(self, dropdown_button_id, dropdown_list_id):
        self.time_sleep(0.5)
        dropdown_button = self.driver.find_element_by_id(dropdown_button_id)
        dropdown_button.location_once_scrolled_into_view
        self.time_sleep(0.5)
        dropdown_button.click()

        dropdown_list = self.driver.find_element_by_id(dropdown_list_id).find_elements_by_tag_name('li')[1]
        dropdown_list.click()

    def insert_text_on_input(self, input_id, wanted_value, is_date = False):
        input_element = self.driver.find_element_by_id(input_id)
        input_element.location_once_scrolled_into_view

        input_element.send_keys(wanted_value)

        if(is_date):
            self.time_sleep(1)
            self.blank_click()
            self.time_sleep(1)

    def send_instance(self):
        for element in self.driver.find_elements_by_xpath('.//span[@class = "ui-button-text ui-c"]'):
            if('Enviar' in element.text):
                element.find_element_by_xpath("..").click()
                return
    
    def select_new_activity(self, activity_index):
        activities_list = self.driver.find_element_by_id('workflowTreeForm').find_element_by_tag_name('div').find_element_by_tag_name('ul').find_element_by_tag_name('li').find_element_by_tag_name('ul').find_element_by_tag_name('li').find_element_by_tag_name('ul').find_elements_by_tag_name('li')[activity_index].find_element_by_tag_name('span').find_elements_by_tag_name('span')
        activities_list[2].click()
    
    def blank_click(self):
        actions = ActionChains(self.driver) 
        actions.send_keys(Keys.TAB)
        actions.perform()

    def time_sleep(self, wanted_seconds):
        time.sleep(wanted_seconds)
