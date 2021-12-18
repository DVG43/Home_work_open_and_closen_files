import os
# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }
# my_file = open("BabyFile.txt", "w+")
# my_file.write("Привет, файл!")
# my_file.close()

# my_file = open ("coock_book.txt","w+")
# my_file.write("Все ОК")
# my_file.close()

#

def get_data_dishes(file_neme):
      dishes_list = []
      with open(file_neme,encoding='UTF-8') as file:
            for line in file:
                  dishes_list.append(line.strip())
                  dish_qantity = int(file.readline().strip())
                  for ingradients in range(dish_qantity):
                        file.readline()
                  file.readline()
      return dishes_list

def get_data_ingrediens(file_neme):
      ingredies_list = []
      with open(file_neme,encoding='UTF-8') as file:
            for line in file:
                  list_ingr = []
                  ingredies_list.append(list_ingr)
                  dish_qantity = int(file.readline().strip())
                  for ingradients in range(dish_qantity):
                        ingradients = file.readline().strip()
                        list_ingr.append(ingradients)
                  file.readline()
      return ingredies_list

def make_dict_from_str(str_name):
      new_str = str_name.split("|")
      new_dickt = {'ingredient_name': new_str[0], 'quantity': new_str[1], 'measure': new_str[2]}
      return new_dickt

print(get_data_dishes("starting_file.txt"))
print()
list_of_list = get_data_ingrediens("starting_file.txt")
new_list_of_list = []
for elements_list_of_list in list_of_list:
      for parts_elements_list_of_list in elements_list_of_list:


print(list_of_list)