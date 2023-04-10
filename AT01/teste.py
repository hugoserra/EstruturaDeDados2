def selection_sort(array, n):

    if n == 1:
        return array

    minimo = 0
    for i in range(1, n):
        if array[i] < array[minimo]:
            minimo = i

    array[0], array[minimo] = array[minimo], array[0]

    selection_sort(array[1:], n-1)

    return array

array = [5,6,7,8,2,3,4,1,5,6,7,8]
array_ordenada = selection_sort(array, len(array))
print("array ordenada: ", array_ordenada)
