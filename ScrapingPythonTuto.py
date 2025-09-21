import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin
FinalScrapingPythonTuto={}

def ResumeSujet(link):
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
    }
    response = requests.get(link,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    divv=soup.find('div', class_='entry-content')
    section=divv.findAll('ul', class_='wp-block-list')
    resumerList = []
    for i in range(len(section)):
        if i==len(section)-1:
            for j in section[i].findAll('li'):
                resumerList.append(j.get_text())
    resumer = "\n".join(resumerList)
    return resumer

def addCategorie(link,Title):
    global FinalScrapingPythonTuto
    finalcat={}
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
    }
    response = requests.get(link,headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    Final={}
    for div in soup.findAll('div', class_='entry-content'):
        for divv in div.findAll('div', class_='wp-block-group'):
            titref = divv.find('h2', class_='wp-block-heading')
            titre = titref.get_text(strip=True)
            liens = []
            for lien in divv.find_all("a", href=True):
                sous_lien = urljoin(link, lien["href"])
                texte = lien.get_text(strip=True)
                liens.append([sous_lien, texte])
            Final[titre[:-1]] = liens
    print(f"-------------------------------------------{Title}-------------------------------------------")
    for title in Final.keys():
        finalcat[title] =[]
        print(title)
        for lien in Final[title]:
            if lien[1]=="#":
                finalcat[title].append({"Name": "Introduction", "resume": RfesumeSujet(lien[0]), "link": lien[0]})
            else:
                finalcat[title].append({"Name":lien[1],"resume":ResumeSujet(lien[0]),"link":lien[0]})
    FinalScrapingPythonTuto[Title]=finalcat

addCategorie("https://www.pythontutorial.net/python-basics/","Python Basics")
addCategorie("https://www.pythontutorial.net/python-oop/","Python OOP")
addCategorie("https://www.pythontutorial.net/python-concurrency/","Python Concurrency")
addCategorie("https://www.pythontutorial.net/advanced-python/","Advanced Python")
addCategorie("https://www.pythontutorial.net/python-regex/","Python Regex")
addCategorie("https://www.pythontutorial.net/python-unit-testing/","Unit Testing")
addCategorie("https://www.pythontutorial.net/python-numpy/","NumPy")
addCategorie("https://www.pythontutorial.net/tkinter/","Tkinter")
addCategorie("https://www.pythontutorial.net/pyqt/","PyQt")
addCategorie("https://www.pythontutorial.net/django-tutorial/","Django")

with open('FinalScrapingPythonTuto.json', 'w', encoding='utf-8') as json_file:
    json.dump(FinalScrapingPythonTuto, json_file, ensure_ascii=False, indent=4)


