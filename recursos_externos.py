from openpyxl import Workbook, load_workbook

# Informações de Login
senha = 'Vendermuito@1005'
usuario = 'mahinavacationclub'

mensagem = """Olá! Somos da MAHINA TOUR, uma empresa de turismo. Você ama viajar? Quem não ama né! Convidamos você para seguir a nossa página e conhecer nossos vários programas de descontos. Viabilizamos de forma exclusiva a viagem dos seus sonhos, seja sozinho, em família ou com amigos! Venha conferir todas as vantagens de ser um cliente MAHINA! Esperamos por você!!"""


contas = load_workbook("contas.xlsx")

aba_ativa = contas.active

