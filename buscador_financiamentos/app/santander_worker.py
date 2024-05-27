from time import sleep

from modules.browser.browser import Driver
from modules.setup.setup import Setup
from modules.santander.personal_data_page import PersonalDataPage
from modules.personal_data.personal_data import PersonalData


class SantanderWorker(Driver):
    def __init__(self, personal_data):
        # self.driver = Driver()
        self.setup = Setup()
        self.personal_data = personal_data

    def start(self):
        self.personal_data_page = PersonalDataPage(self.personal_data)
        self.personal_data_page.open_page()
        self.personal_data_page.select_pf_pj()
        self.personal_data_page.send_form_itens()
        self.personal_data_page.select_vehicle()
        self.personal_data_page.select_store()
        sleep(10)
