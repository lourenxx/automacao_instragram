from openpyxl import Workbook, load_workbook

# Informações de Login
senha = 'Vendermuito@1005'
usuario = 'mahinavacationclub'


mensagem = """Olá! Somos do Mahina Vacation Club, uma empresa de turismo! Alem dos pacotes de viagens em família, coorporativas e clube de férias, atendemos também viagens escolares. Faremos neste ano nossa viagem de formatura para o Vale Suíço Resort (9° Ano e 3° Médio) e DISNEY WORLD a partir de 2025, com possibilidade de fechamentos de contratos a partir do 5°ano do ensino fundamental . Estamos selecionando pais ou alunos que queiram ser os líderes de turma, podendo ganhar até 100%  de desconto em seu pacote de formatura. Teria interesse em compor nosso time de pais/alunos líderes?"""


contas = load_workbook("contas.xlsx")

aba_ativa = contas.active

