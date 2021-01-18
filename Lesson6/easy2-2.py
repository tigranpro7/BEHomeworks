import os
path = os.getcwd()
nom = 1
for dir in range(9):
    dir_path = os.path.join(path, f'dir_{nom}')
    os.rmdir(dir_path)
    nom +=1