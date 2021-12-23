# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1
# 2.txt
#
# Строка номер 1 файла номер 2
# Итоговый файл:
#
# 2.txt
# 1
# Строка номер 1 файла номер 2
# 1.txt
# 2
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1

file_list = ['new_1.txt', 'new_2.txt','new_3.txt' ]
new_file_list = ['n_new_1.txt', 'n_new_2.txt','n_new_3.txt' ]
new_data_from_files = []
step = 0
while step < len(file_list):
#for some_file in file_list:
     with open(file_list[step],encoding='UTF-8') as f:
          data = f.readlines()
          qvon_str = len(data)
     with open(file_list[step],encoding='UTF-8') as f:
          data_text = f.read()

#for some_file in new_file_list:
     with open(new_file_list[step], 'w') as f:
         f.write(f'{file_list[step]}\n')
         f.write(f'{qvon_str}\n')
         f.write(f'{data_text}\n')
     step +=1
for some_file in new_file_list:
     with open(some_file) as f:
         new_data = f.read()
         new_data_from_files.append(new_data)
new_data_from_files.sort(key=len)
#sorted(new_data_from_files, key=len)
#print(new_data_from_files)


with open('finish_file.txt', 'a') as f:
    for some_pat in new_data_from_files:
          f.write(f'{some_pat}')

# создать список из файловю.
# Открыть три файла в переменные.
# создать список
# отранжировать список по длинне строк
# пройти циклом для формирвоания нового файла
# >>> xs = ['dddd','a','bb','ccc']
# >>> sorted(xs, key=len)
# ['a', 'bb', 'ccc', 'dddd']
