def sorting_algorithm_2(list_of_numbers):
    lenght = len(list_of_numbers)
    for x in range(lenght):
        for y in range(0, lenght - x - 1):
            if list_of_numbers[y] > list_of_numbers[y + 1]:
                list_of_numbers[y], list_of_numbers[y + 1] = list_of_numbers[y + 1], list_of_numbers[y]
    return list_of_numbers


print(sorting_algorithm_2([3, 2, 9, 7]))
