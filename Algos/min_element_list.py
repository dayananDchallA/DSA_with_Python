def min_element_list(list):
    min_element = list[0]
    for i in range(1, len(list)):
        if list[i] < min_element:
            min_element = list[i]
    return min_element

print(min_element_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(min_element_list([2,23,45,65,67,89,90]))