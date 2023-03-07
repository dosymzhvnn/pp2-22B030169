import os

print("Текущая директория: " , os.getcwd())
path = r'C:/Users/dosya/OneDrive/Документы/GitHub/pp2-22B030169/tsis6'
print(os.listdir())


print('Cписок каталогов и файлов')
for dirpath, dirnames , files in os.walk(path):
    for dirname in dirnames:
        print('Каталог: ' , os.path.join(dirpath , dirname))
    for filename in files:
        print('Файл: ' , os.path.join(dirpath, filename)) 
  
        
print('Cписок каталогов')       
for dirpath, dirnames in os.walk(path):
    for dirname in dirnames:
        print('Каталог: ' , os.path.join(dirpath , dirname))
    
        
print('Cписок файлов')
for dirpath, files in os.walk(path):      
    for filename in files:
        print('Файл: ' , os.path.join(dirpath, filename)) 
