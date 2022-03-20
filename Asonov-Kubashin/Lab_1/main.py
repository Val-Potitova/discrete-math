# объединение множеств
def sets_union(array1, array2):
    result_set = array1.union(array2)
    result_set = sorted(result_set)
    return result_set


# пересечение множеств
def intersection(array1, array2):
    result_set = array1 & array2
    result_set = sorted(result_set)
    return result_set


# разность множеств
def difference(array1, array2):
    result_set = array1 - array2
    result_set = sorted(result_set)
    return result_set


# симметричная разность
def symmetric_difference(array1, array2):
    result_set = array1 ^ array2
    result_set = sorted(result_set)
    return result_set


# массив 1 дополняется до массива 2
def addition(array1, array2):
    result_set = array2 - array1
    result_set = sorted(result_set)
    return result_set


# Построение булеана
def boolean(array):
    length = len(array)
    # цикл по маскам
    for n in range(1, 2**length):
        b = ""
        # перевод маски в двоичную сс
        while n > 0:
            b = str(n % 2) + b
            n = n // 2
        while len(b) < length:
            b = '0'+b
        j = 0
        temp = {}
        temp = set(temp)
        for i in array:
            if b[j] == "1":
                temp.add(i)
            j += 1
        print(*temp)



if __name__ == "__main__":
    array_A = set(input("Введите через пробел элементы множества 1: ").split(" "))

    array_B = set(input("Введите через пробел элементы множества 2: ").split(" "))

    print(array_A)

    print("u : объединение множеств \n"
          "i : пересечение множеств \n"
          "s : разность множеств 1-2 \n"
          "s- : симметрическая разность множеств \n"
          "a : дополнение множества 1 до множества 2 \n"
          "b - булеан множества 1")
    operation = input()

    if operation == "u":
        print(*sets_union(array_A, array_B))
    if operation == "i":
        print(*intersection(array_A, array_B))
    if operation == "s":
        print(*difference(array_A, array_B))
    if operation == "s-":
        print(*symmetric_difference(array_A, array_B))
    if operation == "a":
        print(*addition(array_A, array_B))
    if operation == "b":
        print(boolean(array_A))
