import requests
from bs4 import BeautifulSoup

head = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 OPR/77.0.4054.90'}

cidade = input("Clima da cidade de: ")

link = requests.get(f'https://www.google.com/search?client=opera-gx&q=clima+{cidade}&sourceid=opera&ie=UTF-8&oe=UTF-8', headers=head)
bs = BeautifulSoup(link.content, 'html.parser')

ceu = bs.find('div', attrs={'class':'wob_dcp'}).get_text()        #Estado do ceu. e.g(Nublado, limpo, sol)
lga = bs.find('div', attrs={'class':'wob_loc mfMhoc'}).get_text() #Cidade
tmp = bs.find('span', attrs={'class':'wob_t TVtOme'}).get_text()  #Temperatura atual

chv = bs.find('div', attrs={'class':'wtsRwe'}).findChild('span', attrs={'id':'wob_pp'}).get_text()    #% de chuva
umi = bs.find('div', attrs={'class':'wtsRwe'}).findChild('span', attrs={'id':'wob_hm'}).get_text()    #% de umidade
vnt = bs.find('div', attrs={'class':'wtsRwe'}).findChild('span', attrs={'class':'wob_t'}).get_text()  #Velocidade do vento

tmpmax = bs.find('div', attrs={'class':'wob_df wob_ds'}).findChild('div', attrs={'class':'vk_gy gNCp2e'}).findChild('span', attrs={'class':'wob_t'}).get_text()   #Temperatura maxima no dia
tmpmin = bs.find('div', attrs={'class':'wob_df wob_ds'}).findChild('div', attrs={'class':'QrNVmd ZXCv8e'}).findChild('span', attrs={'class':'wob_t'}).get_text()  #Temperatura minima no dia

print(f"""
Hoje em {lga} está {ceu} com sensação de {tmp} graus.

Agora estamos com:
{chv} de chance de chuva.
Ventos de {vnt}.
Umidadade de {umi}.

A temperatura maxima prevista para hoje é de {tmpmax} graus e a minima de {tmpmin} graus.
""")
