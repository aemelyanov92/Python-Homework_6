# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.


from random import randint


def more_then(num):
    first_list = [randint(0, 1000) for _ in range(num)]
    print(first_list)
    return [num for i, num in enumerate(first_list[1:]) if num > first_list[i]]


print(more_then(int(input())))
