def merge(array):
    if len(array) <= 1:
        return array
    
    middle_point = len(array) // 2
    right_part = merge(array[middle_point:])
    left_part = merge(array[:middle_point])


    left_array_index = 0
    right_array_index = 0
    sorted_array = []

    while left_array_index < len(left_part) and right_array_index < len(right_part):
        if left_part[left_array_index] < right_part[right_array_index]:
            sorted_array.append(left_part[left_array_index])
            left_array_index += 1
        else:
            sorted_array.append(right_part[right_array_index])
            right_array_index += 1
        
    sorted_array.extend(left_part[left_array_index:])
    sorted_array.extend(right_part[right_array_index:])
    return sorted_array
        


numbers =  [4, 10, 6, 14, 2, 1, 8, 5]
sorted_array = merge(numbers)
print(sorted_array)