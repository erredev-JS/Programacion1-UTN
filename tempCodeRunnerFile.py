def insertion_sort_large(to_order):
    for i in range(1, len(to_order)):
        key = to_order[i]  
        j = i - 1  

        while j >= 0 and key < to_order[j]:
            to_order[j + 1] = to_order[j]
            j -= 1

        to_order[j + 1] = key

num_list = [5, 8, 9, 3, 1, 4, 5, 8, 7, 5, 5, 185, 5, 15, 16, 5163, 4658, 463, 516, 84]

insertion_sort_large(num_list)
print(num_list)
