import re
from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv


## Читаем адресную книгу в формате CSV в список contacts_list:

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
#pprint(contacts_list)

pattern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
replace = r'+7(\2)\3-\4\5 \6\7'

def main(contacts_list: list):
    list_1 = list()
    for t in contacts_list:
        sub = re.sub(pattern, replace, t[5])
        name = ' '.join(t[:3]).split(' ')
        result = [name[0], name[1], name[2], t[3], t[4], sub, t[6]]


        list_1.append(result)
        #print(t)
        #pprint(list_1)


            #print(list_2)
    return union(list_1)


#pprint(contacts_list)

def union(contacts: list):
    for contact in contacts:
        first_name = contact[0]
        last_name = contact[1]

        for new_contact in contacts:
            #print(new_contact)
            new_first_name = new_contact[0]
            new_last_name = new_contact[1]
            #print(new_first_name)
            if first_name == new_first_name and last_name == new_last_name:
                if contact[2] == "": contact[2] = new_contact[2]
                if contact[3] == "": contact[3] = new_contact[3]
                if contact[4] == "": contact[4] = new_contact[4]
                if contact[5] == "": contact[5] = new_contact[5]
                if contact[6] == "": contact[6] = new_contact[6]



    result_list = list()


    for i in contacts:
        #print(i[0])
        if i not in result_list:
            result_list.append(i)
        #    print(i)

    return result_list




## 1. Выполните пункты 1-3 задания.
## Ваш код

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
#

#print(contacts_list)
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(main(contacts_list))
