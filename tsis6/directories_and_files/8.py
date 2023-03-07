import os

path = r'C:/Users/dosya/OneDrive/Документы/GitHub/pp2-22B030169/1.py'

if os.path.exists(path):
    os.remove(path)
    print('Файл существует и будет удален!')
else:
    print('Файл с таким именем не существует!')