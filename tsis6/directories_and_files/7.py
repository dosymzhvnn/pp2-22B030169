import os

with open('A.txt' , 'r') as source_file ,open('копия_файлаA.txt', 'w') as destination_file:
    копирование = source_file.read()
    destination_file.write(копирование)
    
    
print('Скопировано!')