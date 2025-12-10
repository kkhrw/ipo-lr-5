import re
try:
 with open("text.txt","r", encoding = "utf-8") as file:
    text = file.read()
except FileNotFoundError:
    print("Файл не найден")   
else:
    words = text.split()
    print(len(words))  
