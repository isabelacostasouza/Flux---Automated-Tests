import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class FluxTester():
    def __init__(self):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--no-sandbox')
        # chrome_options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="./chromedriver")
        return
    
    def login_on_dev(self, username, password):
        self.driver.get('http://dev.luar.dcc.ufmg.br/')

        username_element = self.driver.find_element_by_id("loginForm:login")
        username_element.send_keys(username)

        password_element = self.driver.find_element_by_id("loginForm:password")
        password_element.send_keys(password)
        
        login_button = self.driver.find_element_by_id("loginForm:j_id_t")
        login_button.click()

    def select_workflow(self, workflow_name):
        self.driver.get('http://dev.luar.dcc.ufmg.br/workflowSelection')

        for element in self.driver.find_elements_by_xpath('.//span[@class = "ui-panel-title"]'):
            if(workflow_name in element.text):
                element.find_element_by_xpath("../../..").click()
                return

    def create_instance(self):
        create_instance_buttton = self.driver.find_element_by_id('j_id_4g:instanceSelectionForm:j_id_4u')
        create_instance_buttton.click()

    def select_first_radiobox_option(self, radiobox_id):
        radiobox_options = self.driver.find_element_by_id(radiobox_id).find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('div')
        radiobox_options[0].click()

    def select_first_dropdown_option(self, dropdown_button_id, dropdown_list_id):
        dropdown_button = self.driver.find_element_by_id(dropdown_button_id).find_elements_by_tag_name('button')[0]
        dropdown_button.click()

        self.driver.implicitly_wait(2)

        dropdown_list = self.driver.find_element_by_id(dropdown_list_id)
        dropdown_list.click()

    def insert_text_on_input(self, input_id, wanted_value):
        input_element = self.driver.find_element_by_id(input_id)
        input_element.send_keys(wanted_value)

    def send_instance(self):
        for element in self.driver.find_elements_by_xpath('.//span[@class = "ui-button-text ui-c"]'):
            if('Enviar' in element.text):
                element.find_element_by_xpath("..").click()
                return

    def time_sleep(wanted_seconds):
        time.sleep(wanted_seconds)
