import os


# new_file = os.mkdir(r'C:/Users/dosya/OneDrive/Документы/GitHub/pp2-22B030169/tsis6/directories_and_files/5py.py')
file = r'C:/Users/dosya/OneDrive/Документы/GitHub/pp2-22B030169/tsis6'

with open("5.py" , "w") as file:
    for dirpath, files in os.walk(file):      
        for filename in files:
            os.write('Файл: ' , os.path.join(dirpath, filename)) 
