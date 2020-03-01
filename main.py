import pprint
cook_book ={}

def read_book(filename):
    cook_book ={}

    with open(filename, encoding="utf8") as f:
        raw_book = f.readlines()
    while len(raw_book) > 0:
        dish = raw_book.pop(0).strip()
        ing_count = int(raw_book.pop(0).strip())
        ingredient_list = []
        for i in range(ing_count):
            ingr_info = [x.strip() for x in raw_book.pop(0).split("|")]
            ingr_info[1] = int(ingr_info[1])
            ingredient_list.append(dict(zip(['ingredient_name', 'quantity', 'measure'],ingr_info)))
        cook_book[dish]=ingredient_list
        while len(raw_book) > 0 and raw_book[0].strip() == '':  # delete empty lines after dish block
            raw_book.pop(0)
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    needed_ingr ={}
    ingr_all = []
    for dish in dishes:
        ingr_all += [ingr for ingr in cook_book[dish]]
    for new_ingr in ingr_all:
        if new_ingr['ingredient_name'] in needed_ingr.keys():  # update quantity
            assert needed_ingr[new_ingr['ingredient_name']]['measure'] == new_ingr['measure'], "Different measures of ingredients, I can't count it!"
            needed_ingr[new_ingr['ingredient_name']]['quantity'] += new_ingr['quantity']
        else:  # add new ingredient if not in dict
            needed_ingr[new_ingr['ingredient_name']] = {'measure': new_ingr['measure'], 'quantity': new_ingr['quantity']}

    # consider the count of person
    for ingr_name in needed_ingr:
        needed_ingr[ingr_name]['quantity'] *= person_count

    return needed_ingr


cook_book = read_book('recipes.txt')
#needed_ingr = get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Утка по-пекински'], 2)
needed_ingr = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
# print(cook_book)

pprint.pprint(needed_ingr)

