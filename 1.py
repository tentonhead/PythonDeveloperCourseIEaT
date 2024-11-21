numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
none_index = 0
for i in range(len(numbers)):
    if numbers[i] == None:
        none_index = i
        numbers[none_index] = 0
        break

avg = sum(numbers) / len(numbers)
numbers[none_index] = avg
print("Измененный список:", numbers)
