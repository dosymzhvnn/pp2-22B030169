import os

path = r'C:/Users/dosya/OneDrive/Документы/GitHub/pp2-22B030169'
file = r'tsis6'

if os.path.exists(file):
    dirname, filename = os.path.split(path)
    print("Directory:", dirname)
    print("Filename:", filename)
else:
    print('Файл не существует!')