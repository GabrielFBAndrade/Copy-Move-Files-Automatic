#importar as bibliotecas
import os
import shutil

# Caminhos dos diretórios
original_folder = 'C:/Users/gabri/OneDrive/Área de Trabalho/Programming Projects/Copy-Move-Files-Automatic/C'
A_folder = 'C:/Users/gabri/OneDrive/Área de Trabalho/Programming Projects/Copy-Move-Files-Automatic/A'
B_folder = 'C:/Users/gabri/OneDrive/Área de Trabalho/Programming Projects/Copy-Move-Files-Automatic/B'

# Função para mover arquivos para os diretórios A e B
def move_file(file, source_folder, target_folder):
    print(file)
    filename = os.path.join(source_folder, file)
    
    if os.path.exists(filename):
        print(filename)
        shutil.move(filename, target_folder)
        print(len(os.listdir(target_folder)))

# Iteração sobre os arquivos
for dirs, subdirs, files in os.walk(original_folder):
    for file in files:
        if os.path.basename(file).startswith('A'): #define o parâmetro para seleção do arquivo
            move_file(file, original_folder, A_folder) #move os arquivos para a pasta desejada com base na condição definina
        else:
            move_file(file, original_folder, B_folder)
