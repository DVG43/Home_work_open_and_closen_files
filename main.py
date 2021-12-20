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

# достаем из файла названия блюд и формируем список
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

# достаем из файла инградиенты
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

def make_list_of_dict(list_list):
      new_list_of_dict = []
      for element_list in list_list:
            new_element_list = []
            for element_str in element_list:
                 new_element_list.append(make_dict_from_str(element_str))
                 #new_element_list.append('\n')
            new_list_of_dict.append(new_element_list)
            #new_list_of_dict.append('\n')
      return new_list_of_dict

#print(get_data_dishes("starting_file.txt"))
#print()
list_of_list = get_data_ingrediens("starting_file.txt")
#print(list_of_list)
new_list_of_list = make_list_of_dict(list_of_list)
#print(new_list_of_list)


dishes_name_lis = get_data_dishes("starting_file.txt")
# Генератор словаря из двух списков
cook_book = {(key_dishes_name_lis): (value_list_of_list) for key_dishes_name_lis in dishes_name_lis
             for value_list_of_list in new_list_of_list }


print(cook_book)

#  get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }
whishes_list = []
persons = 0
def get_shop_list_by_dishes (whishes_list, persons):
# Проверка правильости блюда по переменной dishes_name_lis - цикл по списку ввода.
      total_list_whishes = []
      total_list_ingredient = []
      for dish_name in whishes_list:
            if dish_name in dishes_name_lis:
                  # добавляем в АА переменную А
                  # добавляем в BB переменную B
                   total_list_whishes.append(dish_name)
                   total_list_ingredient.append(make_value_new_dict(dish_name,cook_book))
            else:
                  print (f'Блюда {dish_name} нет в кухонной книге')
      # Генерируем словарь из двух списков.
      new_dict_of_dish_for_persons = {(key_new_dict): (value_new_dict) for key_new_dict in total_list_whishes
                                      for value_new_dict in total_list_ingredient }
      return  new_dict_of_dish_for_persons

def make_value_new_dict(name_in_dict, some_dict):
      list_of_ingradient = some_dict['name_in_dict']
      new_list_of_ingradient = []
      for name_of_ingradient in  list_of_ingradient:
            aaa = name_of_ingradient ['measure']
            bbb = name_of_ingradient ['quantity']*persons
            ingradient_dict = {'measure': aaa , 'quantity': bbb  }
            new_list_of_ingradient.append(ingradient_dict)


# Определяем B [].
# цикл по списку значения подфункция с формированием  словаря для значений
 #     удаляем первый ключ
#      меняем местами второй и третий ключ
#      умножаем значение третьего ключа на глобальную переменную - количество персон.
#      Добавляем словарь в переменную В
# возвращает переменую B

# Печатаем словарь
print ( get_shop_list_by_dishes (whishes_list, persons))







# Подфункция как параметр вводится список со словарями.
# Определяем А [].

# Выбираем значения по ключу.
# цикл по списку значения подфункция с формированием переменной для ключа и словаря для значения
#      вытаскиваем значение первого ключа в переменную А
#      добавляем пеерменную А в список ингрединетов
# # возвращает переменую А

# Определяем B [].
# цикл по списку значения подфункция с формированием  словаря для значений
 #     удаляем первый ключ
#      меняем местами второй и третий ключ
#      умножаем значение третьего ключа на глобальную переменную - количество персон.
#      Добавляем словарь в переменную В
# возвращает переменую B








