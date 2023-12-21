# функция_для_деления_массива_на_заданные_куски/# function_for_division_of_array_into_defined_chunks
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 #делим_длинну_на_две_части/#divide_length_into_two_parts
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

# функция_для_сравнения_чисел_кусках_и_сборка_отсортированного_массива
# #function_for_comparing_numbers_of_bites_and_assembling_the_sorted_array
def merge(left, right):
    result = [] #переменная_с_пустым_списком / #variable_with_empty_list
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right): #Пока левый индекс меньше длинны левой стороны и правый индекс меньше длинны правой стороны
        # While the left index is less than the length of the left side and the right index is less than the length of the right side
        if left[left_index] < right[right_index]: #Если левый индекс меньше правого/#If the left index is less than the right index
            result.append(left[left_index]) #В результат добавляем левый индекс/#Add the left index to the result
            left_index += 1
        else: #Наоборот/#On the contrary
            result.append(right[right_index])
            right_index += 1

    if left_index < len(left): #Если левый индекс меньше количества левой стороны/#If the left index is less than the left side quantity
        result.extend(left[left_index:]) #В результат дополняем в левую сторону/#The result is augmented to the left side
    elif right_index < len(right): #Наоборот/#On the contrary
        result.extend(right[right_index:])

    return result

arr = [5, 2, 8, 3, 9, 1]
sorted_arr = merge_sort(arr)
print(f"'Сортировка слиянием': {sorted_arr}")
