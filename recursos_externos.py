from openpyxl import Workbook, load_workbook

# Informações de Login
senha = ''
usuario = ''


mensagem = """ """

contas = load_workbook("contas.xlsx")

aba_ativa = contas.active

