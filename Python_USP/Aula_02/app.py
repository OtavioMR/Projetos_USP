import pandas as pd
import numpy as np
import os

diretorio = r'C:\Users\GiovannaMayumiSakaiS\Downloads\\'
nome_do_arquivo = 'Região de Solânea.xlsx'
caminho_completo = os.path.join(diretorio, nome_do_arquivo)

dados = pd.read_excel(caminho_completo)
