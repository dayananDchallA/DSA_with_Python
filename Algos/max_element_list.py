def max_element_list(list):
    max_element = list[0]
    for i in range(1, len(list)):
        if list[i] > max_element:
            max_element = list[i]
    return max_element


print(max_element_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(max_element_list([2,23,45,65,67,89,90]))