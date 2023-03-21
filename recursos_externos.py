from openpyxl import Workbook, load_workbook

# Informações de Login
senha = 'JSA18012007'
usuario = 'metamorfoseducacao'

mensagem = """Olá, bom dia! Sou Guilherme Pexirile Lourenço da Colleman The World School. Estamos lançando uma MENTORIA 100% ONLINE sobre EDUCAÇÃO 4.0, caso haja interesse nos mande uma mensagem inbox! Fazemos valores para a divulgação da mentoria em seu perfil e com o cupom GUILHERMEDESC vc garante o valor promocional para ter acesso ao curso mais IMERSIVO sobre a nova educação no Brasil! Obrigado!"""""



contas = load_workbook("contas.xlsx")

aba_ativa = contas.active

