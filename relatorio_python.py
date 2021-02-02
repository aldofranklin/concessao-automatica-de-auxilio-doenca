import PyPDF2
import re

# Abre o arquivo pdf 
# lembre-se que para o windows você deve usar essa barra -> / 
# lembre-se também que você precisa colocar o caminho absoluto
# leitura do arquivo PDF para extração dos parâmetros contidos no arquivo

with open('d:/pythonprojects/sistema_pfe/relatorio_preenchido.pdf', 'rb') as pdf_file:
    resultado = {}
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    pdf_page = pdf_reader.getFields().values()
    for var in pdf_page:
        resultado[var['/T']] = var['/V']



