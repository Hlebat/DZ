numbers = [12, 4, 9, 1, 6, 3]
print("Исходный список:", numbers)
n = len(numbers)
width = 1  # Начинаем с кусочков длиной 1
while width < n:
    for i in range(0, n, 2 * width): # Проходим по списку с шагом 2 * width
        left = numbers[i : i + width] # Берем два соседних кусочка
        right = numbers[i + width : i + 2 * width]
        # Сливаем их обратно в основной список
        l = 0  # индекс для left
        r = 0  # индекс для right
        k = i  # индекс для основного списка
        while l < len(left) and r < len(right): # Сравниваем элементы из left и right
            if left[l] <= right[r]:
                numbers[k] = left[l]
                l += 1
            else:
                numbers[k] = right[r]
                r += 1
            k += 1 
        while l < len(left): # Если в left что-то осталось, дописываем
            numbers[k] = left[l]
            l += 1
            k += 1  
        while r < len(right): # Если в right что-то осталось, дописываем
            numbers[k] = right[r]
            r += 1
            k += 1 
    width *= 2 # Увеличиваем размер кусочков в 2 раза
print("Отсортированный список:", numbers)