#Короленко Ульяна
#вариант 2
filename = "text.txt" #создаем переменную и вписываем значение файла text.txt
filename1 = "output.txt" #создаем переменную и вписываем значение файла output.txt
with open(filename, "r", encoding="utf-8") as filein, open(filename1, "w", encoding="utf-8") as fileout: # блок кода открывает два файла: filein и fileout
  for line in filein: #Этот цикл for перебирает по строкам файла filein
     line = line.strip() #Удаляет пробелы в начале и в конце каждой строки
     if len(line) > 5: #Проверяет, длиннее ли текущая строка line 5 символов
        fileout.write(line + " ") #Если строка line длиннее 5 символов, то она записывается в файл fileout с добавлением пробела в конце.
