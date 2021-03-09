import PySimpleGUI as sg
import re

Texto = sg.popup_get_text('Através da entrada identificaremos a abreviação da UF\nDigite aqui um endereço:', 'Busca UF em texto')
Texto = Texto.upper()
Texto = Texto.replace(", ","-")

def get_ufs(text):
	
   alocastring = r"-(AC|AL|AP|AM|BA|CE|DF|ES|GO|MA|MT|MS|MG|PA|PB|PR|PE|PI|RJ|RN|RS|RO|RR|SC|SP|SE|TO)"
   
   return re.findall(alocastring, text)


print(get_ufs(Texto))

sg.popup('Resultado', 'A abreviação do estado que encontramos no seu texto é', get_ufs(Texto))