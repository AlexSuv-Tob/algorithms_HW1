"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""
base_company = {
    'ya': 2000,
    'gaz': 500,
    'mic': 2300,
    'ros': 50,
    'appel': 2000,
    'ozon': 3000,
    'adidas': 4500,
    'arc': 5500
}
#Первый вариант O(n2)
def sorted_1(random_list):
    for i in range(len(random_list)):
        lowest_valur_index = i
        for j in range(i + 1, len(random_list)):
            if random_list[j][1] > random_list[lowest_valur_index][1]:
                lowest_valur_index = j
        random_list[i], random_list[lowest_valur_index] = random_list[lowest_valur_index], random_list[i]
    return random_list[0:3]
list_from_dic = list(base_company.items())
for i in sorted_1(list_from_dic):
    print(i[0], 't', i[1])

print('#' * 18)

#Второй вариант O(n*logN)

list_from_dic = list(base_company.items())
list_from_dic.sort(key=lambda i: i[1], reverse=True)
for i in range(3):
    print(list_from_dic[i][0], 't', list_from_dic[i][1])

print('#' * 18)

#Третий вариант O(n)

def three_max(list_input):
    input_max = {}
    list_d = dict(list_input)
    for i in range(3):
        maximum = max(list_d.items(), key=lambda k_v: k_v[1])
        del list_d[maximum[0]]
        input_max[maximum[0]] = maximum[1]
    return input_max

print(three_max(base_company))