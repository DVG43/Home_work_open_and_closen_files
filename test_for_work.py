

str_name = 'Яйцо | 2 | шт'
new_str = str_name.split("|")
new_dickt = {'ingredient_name': new_str[0], 'quantity': new_str[1], 'measure': new_str[2]}
print (new_dickt)
