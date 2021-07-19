''''5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().'''

import functools

my_list = [element for element in range(100, 1002, 2)]
def sum_items(previous_item, current_item):
    return previous_item * current_item

print(functools.reduce(sum_items, my_list))