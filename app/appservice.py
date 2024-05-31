# from view.view import View


from app.santander_worker import SantanderWorker

# from app.bv_financeira_worker import BvFinanceiraWorker
# from app.bv_finandigimais_workerceira_worker import DigimaisWorker


from modules.personal_data.personal_data import PersonalData


class BuscadorAppService:
    def __init__(self, personal_data: PersonalData):
        # self.view = View()
        self.personal_data = personal_data
        self.santander_worker = SantanderWorker(self.personal_data)
        # self.bv_financeira_worker = BvFinanceiraWorker(self.personal_data)
        # self.digimais_worker = DigimaisWorker(self.personal_data)

    def start(self):
        # self.personal_data.init_person()
        self.santander_worker.start()
