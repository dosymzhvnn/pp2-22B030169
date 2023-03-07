import os

path = r'C:/Users/dosya/OneDrive/Документы/GitHub/pp2-22B030169/tsis6'

if os.path.exists(path):
    print('Файл существует')
else:
    print('Файл не существует')
    
if os.access(path , os.R_OK):
    print('Файл доступен для чтения')
else:
    print('Файл недоступен для чтения')
    
if os.access(path , os.W_OK):
    print('Файл доступен для записи')
else:
    print('Файл недоступен для записи')
    
if os.access(path , os.X_OK):
    print('файл доступен для выполнения')
else:
    print('Файл недоступен для выполнения')