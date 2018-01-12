#2. Используя Python и модули requests и re написать скрипт,
# получающий все адреса подразделов сайта(относительные url)
#и для каждой из них выполнить поиск адресов электронной почты(см. задание 1)
import requests
from bs4 import BeautifulSoup as BS
import re
links = []
# запрос get для получения информации от сайта
html_page = requests.get('http://www.mosigra.ru/').text
# представление документа вложенной структурой данных
soup = BS(html_page, 'html.parser')
# находит теги, сопоставляя с именем 'a', атрибут href содержит oтносительный URL страницы
href = soup.find_all('a', {'href': re.compile('.+')})
# заполняет список найденных страниц
for tag in href:
    link = tag['href']
    links.append(link)
print(links)
print(len(links))

found = []
found1 = []
found2 = []
found3 = []
# регулярное выражение, которое находит адреса
mailsrch = re.compile(r'[\w.][\w.]+@[\w][\w\.]+[a-zA-Z]{1,4}')
# заполняются списки совпавшими строками
for link in links:
    if link[0:3] == '//w':                        #ищет элемент списка с таким началом
        site = requests.get('http:' + link).text.split(' ') #возвр.сп-к строк разд. проб-м
        for line in site:                          #в сп-ке ищет РВ
            found1 += re.findall(mailsrch, line)   #добавл.зн. к сущ. = нов.зн.

    elif link[0:2] == '//':
        site = requests.get('http:' + link).text.split(' ')
        for line in site:
            found2 += re.findall(mailsrch, line)

    elif link[0] == '/':
        site = requests.get('http://mosigra.ru'+link).text.split(' ')
        for line in site:
            found3 += re.findall(mailsrch, line)
    else:
        pass

    found = found1 + found2 + found3       #все адреса
    found = set(found)
    print(len(found))                     #нашел 53
    print(found)
    viv = open("всеадреса.txt", "w", encoding='utf-8')  #запись в текстовый файл
    v = '\n'
    viv.write(v.join(found))
    viv.close()


