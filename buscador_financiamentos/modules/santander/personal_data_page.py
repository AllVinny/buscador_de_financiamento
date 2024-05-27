from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

from modules.browser.browser import Driver
from modules.setup.setup import Setup
from modules.personal_data.personal_data import PersonalData


class PersonalDataPage(Driver):
    def __init__(self, personal_data):
        super().__init__()
        self.setup = Setup()
        self.personal_data = personal_data

    def open_page(self):
        self.open(self.setup.santander_site)

    def select_pf_pj(self):
        container = self.wait_located(By.XPATH, "//div[@class='container-person']")
        select_pf = container.find_element(By.XPATH, "//button[@class='btn-person']")
        select_pj = container.find_element(
            By.XPATH, "//button[@class='btn-person-legal']"
        )
        if self.personal_data.opt_legal_or_not == "pf":
            select_pf.click()
        if self.personal_data.opt_legal_or_not == "pj":
            select_pj.click()

    def send_form_itens(self):
        complete_form = self.wait_located(By.XPATH, "//div[@class='form']")

        if self.personal_data.opt_legal_or_not == "pf":
            date = "dateOfBirth"
            doc = "cpf"

        if self.personal_data.opt_legal_or_not == "pj":
            date = "dateFoundation"
            doc = "cnpj"

        complete_form.find_element(
            By.XPATH, f"//input[@formcontrolname='{date}']"
        ).send_keys(self.personal_data.date)
        complete_form.find_element(
            By.XPATH, f"//input[@formcontrolname='{doc}']"
        ).send_keys(self.personal_data.cpf_cnpj)
        complete_form.find_element(
            By.XPATH, "//input[@formcontrolname='email']"
        ).send_keys(self.personal_data.email)
        complete_form.find_element(
            By.XPATH, "//input[@formcontrolname='cellNumber']"
        ).send_keys(self.personal_data.phone_number)

        # region cnh
        if (
            self.personal_data.opt_legal_or_not == "pf"
            and self.personal_data.opt_cnh == True
        ):
            complete_form.find_element(By.XPATH, "//label[@for='cnhTrue']").click()

        if (
            self.personal_data.opt_legal_or_not == "pf"
            and self.personal_data.opt_cnh == False
        ):
            complete_form.find_element(By.XPATH, "//label[@for='cnhFalse']").click()
        # endregion

        self.wait_located(By.XPATH, "//button[@class='btn-simulate']").click()
        sleep(5)

    def select_vehicle(self):
        if self.personal_data.opt_vehicle == True:
            self.wait_located(By.XPATH, "//button[@class='btn-vehicle']").click()

        if self.personal_data.opt_vehicle == False:
            self.wait_located(By.XPATH, "//button[@class='btn-motorcycle']").click()

        # self.wait_located(By.XPATH, "//button[@class='btn-simulate']").click()
        sleep(5)

    def select_store(self):
        self.wait_located(
            By.XPATH, "//button[@class='btn-dealership-financing']"
        ).click()
