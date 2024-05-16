try:  # проверка корректности введенных данных
    array = list(map(int , input(
        "Введите последовательность чисел в любом порядке, через пробел: ").split()))  # ввод последовательности чисел
    element = float(input("Введите любое число из заданного диапазона: "))  # ввод произвольного числа
except ValueError:
    print('Ошибка!!! Пожалуйста, вводите только числа!')  # вывод ошибки при вводе некорректных значений
else:
    def bubble_sorting(array):  # сортировка пузырьком
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array


    def binary_search(array, element, left, right):
        if left > right:  # если левая граница превысила правую,
            return False  # значит элемент отсутствует
        middle = (right + left) // 2  # находимо середину
        if array[middle] >= element and array[middle - 1] < element:  # если элемент в середине,
            return middle - 1  # возвращаем этот индекс предидущего элемента
        elif element < array[middle]:  # если элемент меньше элемента в середине
            # рекурсивно ищем в левой половине
            return binary_search(array, element, left, middle - 1)
        else:  # иначе в правой
            return binary_search(array, element, middle + 1, right)


    print('Сортированный список', bubble_sorting(array))
    left = float(array[0])
    right = float(array[-1])
    if element < left or element > right:
        print('Числа нет в диапазоне')
    else:
        print('Индекс элемента, ближайшего минимального от введенного числа ',
              binary_search(array, element, 0, len(array) - 1))
