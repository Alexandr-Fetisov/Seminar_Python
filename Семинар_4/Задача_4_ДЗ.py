# 4. Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо.
# При расшифровке происходит обратная операция.
# К примеру слово:
# "абба" можно зашифровать "бввб" - сдвиг на 1 вправо.
# "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ,
# считывает текст и дешифровывает его.

path1 = "Семинар_4\задача_4_1_ДЗ.txt" # то, что шифруем
path2 = "Семинар_4\задача_4_2_ДЗ.txt" # ЗАшифрованное
path3 = "Семинар_4\задача_4_3_ДЗ.txt" # ДЕшифрованное
temp_list = list()
key = 0

def isint(s):
    """проверка преобразования в число"""
    try:
        int(s)
        return True
    except ValueError:
        return False

def inp(q):
    """проверка ввода корректного числа"""
    while not (isint(q) and (0 < int(q) < 11)):
        q = input("Введите ключ, от 1 до 10 - ")
    return q

def readfile(path):
    """считывает строки из файла, записывает в список"""
    temp_data = list()
    with open (path, 'r', encoding='utf-8') as data:
        for line in data:
            temp_data.append(line)
    return temp_data

def crypto(list_crypto:list,key:int):
    """"шифрует, сдвигая все значения ютф-8 символов списка на значение кей"""
    crypted_list = list()
    splited_list = list()
    for i in list_crypto:
        splited_list.append(list(i))
    for m in splited_list:
        for n in m:
            crypted_list.append(chr(ord(n) + key))       
            
    return crypted_list
    
def rewrite(whatrewrite:list, path):
    """перезаписывает файл списком, каждый элемент с новой строки """
    with open (path, 'w', encoding='utf-8') as data:
        for i in whatrewrite:
            data.writelines(i)

def decrypto(crypted_list, key):
    """"расшифрует, сдвигая все значения ютф-8 символов списка на значение кей"""
    decripted_list = list()
    splited_list = list()
    for i in crypted_list:
        splited_list.append(list(i))
    for m in splited_list:
        for n in m:
            decripted_list.append(chr(ord(n) - key))
    return decripted_list


key = int(inp(key)) # ввели ключ
temp_list = readfile(path1) # Считали текст для шифрования
temp_list = crypto(temp_list, key) # ЗАшифровали
rewrite(temp_list,path2) # ЗАшифрованное записали в файл
temp_list = readfile(path2) # Прочитали ЗАшифрованное
temp_list = decrypto(temp_list,key) # ДЕшифровали
rewrite(temp_list,path3) # ДЕшифрованное записали в файл