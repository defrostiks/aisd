from random import randint

def selection_sort(arr):    # выбором
    for i in range(len(arr)-1):
        minimum_value = arr[i]
        minimum_value_index = i

        for j in range(i+1, len(arr)):  
            if minimum_value > arr[j]:
                minimum_value = arr[j]
                minimum_value_index = j
        if minimum_value_index != i:  
            arr[i], arr[minimum_value_index] = arr[minimum_value_index], arr[i]     

def insertion_sort(arr): # вставками
    for i in range(1,len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:    
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break

def bubble_sort(arr): # пузырьком
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]

def merge_lists(arr_1, arr_2): # функция слияния двух отсортированных массивов
    merge_array = []
    count_1, count_2 = 0, 0
    while count_1 < len(arr_1) and count_2 < len(arr_2):
        if arr_1[count_1] <= arr_2[count_2]:
            merge_array.append(arr_1[count_1])
            count_1 += 1
        else:
            merge_array.append(arr_2[count_2])
            count_2 += 1
    merge_array += arr_1[count_1:] + arr_2[count_2:]
    return merge_array

def merge_sort(arr): # слиянием 
    half_lenght = len(arr)//2   
    split_array_1 = arr[:half_lenght]
    split_array_2 = arr[half_lenght:]
    if len(split_array_1) > 1:
        split_array_1 = merge_sort(split_array_1)
    if len(split_array_2) > 1:
        split_array_2 = merge_sort(split_array_2)
    return merge_lists(split_array_1, split_array_2)

def quick_sort(arr): #быстрая
    if len(arr) > 1:
        random_index = arr[randint(0, len(arr)-1)]
        less = [x for x in arr if x < random_index]
        equal = [x for x in arr if x == random_index]
        great = [x for x in arr if x > random_index]
        arr = quick_sort(less) + equal + quick_sort(great)
    return arr

def shell_sort_shell(arr): # последовательть Шелла
    gap = len(arr)//2
    while gap > 0:
        for value in range(gap, len(arr)):
            temp = arr[value]
            index = value
            while index >= gap and arr[index-gap] > temp:
                arr[index] = arr[index-gap]
                index -= gap
                arr[index] = temp
        gap //= 2
    return arr



def generate_hibbard_sequence(n):
    gaps = []
    k = 1 
    while True:
        gap = (2 ** k) - 1
        if gap >= n:
            break
        gaps.append(gap)
        k += 1 
        gaps.reverse() 
    return gaps

def shell_sort_hibbard(arr):
    n = len(arr)
    gaps = generate_hibbard_sequence(n)
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp



def generate_pratt_sequence(n):
    gaps = []
    i, j = 0, 0
    while True:
        gap = (2 ** i) * (3 ** j)
        if gap > n:
            break
        gaps.append(gap)
        if i < j:  
            j += 1
        else:      
            i += 1 
            gaps.reverse()  
    return gaps

def shell_sort_pratt(arr):
    n = len(arr)
    gaps = generate_pratt_sequence(n)
    for gap in gaps:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp

