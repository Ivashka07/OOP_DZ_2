# with open('text.txt', encoding='utf-8') as f: 
#     for idx, s in enumerate(f):
#         print(idx.s.strip())

# у нас есть cook_book
# 1. Мы запускаем цикл, пока не закончился текстовый документ
# 2. Считываем ключ и помещаем его в ключ словаря
# 3. Считываем n раз ингрдиенты разделив их по |
# 4. Когда наткнемся на новую строку, переходим к 
def get_cook_book(path):
    cook_book = {}

    with open(path, encoding="utf-8") as file:
        lines = file.readlines()

    i = 0
    while i < len(lines):
        dish_name = lines[i].strip()
        ingredient_count = int(lines[i+1].strip())
            
        ingredients = []
        for j in range(ingredient_count):
            ingredient_info = lines[i + 2 + j].strip().split(" | ")
            ingredient = {
                'ingredient_name': ingredient_info[0],
                'quantity': ingredient_info[1],
                'measure': ingredient_info[2],
            }
            ingredients.append(ingredient)
        cook_book[dish_name] = ingredients

        i += ingredient_count + 3
        

    print(*cook_book, sep ='\n')
    return cook_book
print()
cook_book = get_cook_book("text.txt")

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = int(ingredient['quantity']) * person_count

                if name not in shop_list:
                    shop_list[name] = {
                        'measure': measure,
                        'quantity': quantity,
                    }
                else:
                    shop_list[name]['quantity'] += int(quantity)
    return shop_list


print(get_shop_list_by_dishes(["Омлет", "Запеченный картофель"], 2))

