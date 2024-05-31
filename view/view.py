import tkinter as tk
from modules.personal_data.personal_data import PersonalData

from app.appservice import BuscadorAppService


class View(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.personal_data = PersonalData()
        self.buscador_app_service = BuscadorAppService(self.personal_data)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.document_label = tk.Label(self, text="Documento")
        self.document_label.grid(row=0, column=0)
        self.var = tk.StringVar(value="cpf")
        self.cpf_radio = tk.Radiobutton(
            self, text="CPF", variable=self.var, value="cpf"
        )
        self.cpf_radio.grid(row=1, column=0)
        self.cnpj_radio = tk.Radiobutton(
            self, text="CNPJ", variable=self.var, value="cnpj"
        )
        self.cnpj_radio.grid(row=2, column=0)

        self.vehicle_label = tk.Label(self, text="Veículo")
        self.vehicle_label.grid(row=0, column=1)
        self.vehicle_var = tk.StringVar(value="car")
        self.car_radio = tk.Radiobutton(
            self, text="Carro", variable=self.vehicle_var, value="car"
        )
        self.car_radio.grid(row=1, column=1)
        self.motorcycle_radio = tk.Radiobutton(
            self, text="Moto", variable=self.vehicle_var, value="moto"
        )
        self.motorcycle_radio.grid(row=2, column=1)

        self.cnh_label = tk.Label(self, text="CNH")
        self.cnh_label.grid(row=0, column=2)
        self.cnh_var = tk.StringVar(value="yes")
        self.cnh_yes_radio = tk.Radiobutton(
            self, text="Sim", variable=self.cnh_var, value="yes"
        )
        self.cnh_yes_radio.grid(row=1, column=2)
        self.cnh_no_radio = tk.Radiobutton(
            self, text="Não", variable=self.cnh_var, value="no"
        )
        self.cnh_no_radio.grid(row=2, column=2)

        self.document_number_label = tk.Label(self, text="Número de Documento")
        self.document_number_label.grid(row=3, column=0)
        self.document_number_entry = tk.Entry(self)
        self.document_number_entry.grid(row=4, column=0)

        self.birth_date_label = tk.Label(self, text="Data de Nascimento")
        self.birth_date_label.grid(row=3, column=1)
        self.birth_date_entry = tk.Entry(self)
        self.birth_date_entry.grid(row=4, column=1)

        self.email_label = tk.Label(self, text="Email")
        self.email_label.grid(row=3, column=2)
        self.email_entry = tk.Entry(self)
        self.email_entry.grid(row=4, column=2)

        self.phone_label = tk.Label(self, text="Telefone")
        self.phone_label.grid(row=5, column=0)
        self.phone_entry = tk.Entry(self)
        self.phone_entry.grid(row=6, column=0)

        self.button = tk.Button(self, text="Submit", command=self.submit)
        self.button.grid(row=7, column=0, columnspan=3)

    def submit(self):
        if self.var.get() == "cpf":
            self.personal_data.opt_legal_or_not = "pf"
        else:
            self.personal_data.opt_legal_or_not = "pj"

        if self.vehicle_var.get() == "car":
            self.personal_data.opt_vehicle = True
        else:
            self.personal_data.opt_vehicle = False

        if self.cnh_var.get() == "yes":
            self.personal_data.opt_cnh = True
        else:
            self.personal_data.opt_cnh = False

        self.personal_data.document_number = self.document_number_entry.get()
        self.personal_data.birth_date = self.birth_date_entry.get()
        self.personal_data.email = self.email_entry.get()
        self.personal_data.phone = self.phone_entry.get()
        self.buscador_app_service.start()


root = tk.Tk()
app = View(master=root)
app.mainloop()
