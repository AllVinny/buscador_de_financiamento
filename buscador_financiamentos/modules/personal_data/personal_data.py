class PersonalData:
    def __init__(self):
        self.opt_legal_or_not = ""
        self.opt_cnh = ""
        self.opt_vehicle = ""
        self.date = ""
        self.cpf_cnpj = ""
        self.email = ""
        self.phone_number = ""

    def init_person(self):
        self.set_person()
        self.set_data()

    def set_person(self):
        while self.opt_legal_or_not not in [1, 2]:
            self.opt_legal_or_not = int(
                input("Selecione o documento: \n 1- CPF \n 2- CNPJ\n")
            )
            if self.opt_legal_or_not not in [1, 2]:
                print("Digite a opção 1 ou 2! ")
                continue
            if self.opt_legal_or_not == 1:
                self.opt_legal_or_not = "pf"
                break
            if self.opt_legal_or_not == 2:
                self.opt_legal_or_not = "pj"
                break

        while self.opt_cnh not in [1, 2]:
            self.opt_cnh = int(input("Possui CNH: \n 1- Sim \n 2- Não\n"))
            if self.opt_cnh not in [1, 2]:
                print("Digite a opção 1 ou 2! ")
                continue
            if self.opt_cnh == 1:
                self.opt_cnh = True
                break
            if self.opt_cnh == 2:
                self.opt_cnh = False
                break

        while self.opt_vehicle not in [1, 2]:
            self.opt_vehicle = int(input("Qual o veículo: \n 1- Carro \n 2- Moto\n"))
            if self.opt_vehicle not in [1, 2]:
                print("Digite a opção 1 ou 2! ")
                continue
            if self.opt_vehicle == 1:
                self.opt_vehicle = True
                break
            if self.opt_vehicle == 2:
                self.opt_vehicle = False
                break

    def set_data(self):
        self.date = "13/09/1998"
        self.cpf_cnpj = "46525458862"
        self.email = "neutro@email.com"
        self.phone_number = "99999999999"
