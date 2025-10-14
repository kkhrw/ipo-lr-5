#Короленко Ульяна
#Вариант 2
with open ("text.txt", "r", encoding="utf-8") as file: #oткрываем файл
    a = file.read() #cохраняем данные файла в переменной a
    list = a.split() #cохраняем слова в список b
    with open ("output.txt", "w", encoding="utf-8") as file1: #oткрываем файл
        for i in list: #перебор списка
            if len(i) > 5: #условие
                file1.write(str(i)) #записываем элемент i в файл