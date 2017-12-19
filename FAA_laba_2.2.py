import re
import requests


def get_adr(new_adr, seen):    #функция, котороя ищет все страницы сайта
    words = [
             q
            for i in range(len(new_adr))                          #для каждого элемента переменной-списка
            for text in requests.get(new_adr[i]).text.split(' ')  #записывает информацию с сайта в виде списка слов
            for q in re.findall('href="/.+/"', text)              #находит в тексте по регулярным выражениям все страницы сайта
            ]
    words = {                      #выбрасывает повторяющиеся элементы списка, записывает их как абсолютные адреса
             'http:/' + words[i][7:len(words[i]) - 2] + '/'
             if words[i][7] == '/'
             else 'http://www.mosigra.ru/' + words[i][7:len(words[i]) - 2] + '/'
             for i in range(len(words))
            }
    new_adr = [                    #записывает в список new_adr те страницы, которых нет в списке seen
            x
            for x in words
            if x not in seen
            ]
    for x in words:               #записывает в seen те страницы, которых там нет
        if x not in seen:
            seen.append(x)
    if len(new_adr) > 2:          #запуск рекурсии
        get_adr(new_adr, seen)
    else:                         #записывает все страницы сайта в тексторый файл, каждый в отдельную строку
        put = open("all_адреса_сайта_тест.txt", "w", encoding='utf-8')
        put.write('\n'.join(seen))
        put.close()
        return seen


def adr_mail(c):             #функция, которая ищет все адреса электронной почты(уникальные) из всех страниц сайта
    words = {
             q
            for gr_1 in range(len(c))
            for text in requests.get(c[gr_1]).text.split(' ')    #информация со страницы записывается в текст
            for q in re.findall('[\w.][\w.]+@\w+\.\w+', text)    #находит в тексте электронные адреса
            }
    viv = open("сортированные_почты.txt", "w", encoding='utf-8')  #запись электронных адресов в текстовый файл
    viv.write('\n'.join(words))
    viv.close()

arr_link = get_adr(['http://www.mosigra.ru/'], ['http://www.mosigra.ru/']) #вызов функции с передачей стартовой страницы в виде списка
o = adr_mail(arr_link)

print (o)



# print(words[10])
#
# words = [
#             'http:/' + words[i][7:len(words[i]) - 1]
#             if words[i][7] == '/'
#             else 'http://www.mosigra.ru/' + words[i][7:len(words[i]) - 1]
#             for i in range(len(words))
#         ]
# words = list(words)
#
# print(words[10])
#
# new_adr = []
#
# for x in words:
#     if x not in seen:
#         new_adr.append(x)
#
# for x in words:
#     if x not in seen:
#         seen.append(x)
#начало 2-й итерации рекурсии

# words = []
# for i in range(len(new_adr)):
#
#     for text in requests.get(new_adr[i]).text.split(' '):
#         for q in re.findall('href="/.+/"', text):
#             words.append(q)
#             # print(q)
#             # print("пикабу///////////////////////////////")
#
# words = {
#             'http:/' + words[i][7:len(words[i]) - 2] + '/'
#             if words[i][7] == '/'
#             else 'http://www.mosigra.ru/' + words[i][7:len(words[i]) - 2] + '/'
#             for i in range(len(words))
#         }
# words = list(words)
#
# #new_adr = [x for x in words if x not in seen]
# print(len(words))
# print(len(seen))
# print(len(new_adr))
#
# new_adr = []
#
# for x in words:
#     if x not in seen:
#         new_adr.append(x)
#
# for x in words:
#     if x not in seen:
#         seen.append(x)
#
# print(len(new_adr))
# print(len(seen))
