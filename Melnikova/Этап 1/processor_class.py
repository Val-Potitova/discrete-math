# Процессор числовых множеств (без помощи множеств...)

class Set:
    def __init__(self, s=''):
        if s == '':
            print('Введите через пробел элементы множества')
            s = input()

        def toInt(element):
            return int(element)

        s = s.split(' ')
        arr = list(map(toInt, s))
        self.set_arr = sorted(list(set(arr)))
        self.count_subsets()

    def __str__(self):
        return f"Ваше множество: {self.set_arr}"

    # пересечение множеств
    def intersection(self, other):
        if type(other) != Set:
            return "Операция доступна только для множеств!!!"
        else:
            intersect = []
            for i in self.set_arr:
                if i in other.set_arr:
                    intersect.append(i)
            return intersect

    # объединение множеств
    def union(self, other):
        if type(other) != Set:
            return "Операция доступна только для множеств!!!"
        else:
            uni = self.set_arr
            for i in other.set_arr:
                uni.append(i)
            return sorted(list(set(uni)))

    # дополнение множества self до other
    def update(self, other):
        if type(other) != Set:
            return "Операция доступна только для множеств!!!"
        else:
            elementsInBoth = []
            for i in self.set_arr:
                if i in other.set_arr:
                    elementsInBoth.append(i)
            if elementsInBoth == self.set_arr:
                res = []
                for i in other.set_arr:
                    if not (i in elementsInBoth):
                        res.append(i)
                return res
            else:
                return f"Дополнить множество {self.set_arr} до множества {other.set_arr} невозможно"

    # разность self\other
    def difference(self, other):
        if type(other) != Set:
            return "Операция доступна только для множеств!!!"
        else:
            d = []
            for i in self.set_arr:
                if i not in other.set_arr:
                    d.append(i)
            return d

    # симметрическая разность self\other
    def symmetric_difference(self, other):
        if type(other) != Set:
            return "Операция доступна только для множеств!!!"
        else:
            u = self.union(other)
            inter = self.intersection(other)
            symm_d = []
            for i in u:
                if i not in inter:
                    symm_d.append(i)
            return symm_d

    # функция, возвращающая количество подмножеств множества self
    def count_subsets(self):
        subs, subsets = [], []
        for i in range(2 ** len(self.set_arr)):
            subs.append((bin(i)[2:]).zfill(len(self.set_arr)))
        for i in subs:
            sub = []
            for j in range(len(self.set_arr)):
                if i[j] == '1':
                    sub.append(self.set_arr[j])
            subsets.append(sub)
        self.subsets = (sorted(subsets, key=len))
        return len(self.subsets)


if __name__ == '__main__':
    # Инициализируем три множества и переменную для проверки типизации
    # В классе доступен ввод множеств с клавиатуры, если мы не передаем строку с числами
    a = Set('1 2 3 4')
    b = Set('11 3 4 5')
    c = Set('1 2 3 4 5 6')
    h = 'hello'

    # Выведем информацию о множестве a и всех его подмножествах
    print(a)
    print(f"Подмножества множества а: {a.subsets}")
    print(f"Количество элементов 2^a: {a.count_subsets()}", "\n")

    print(f"a∩b = {a.intersection(b)}")
    print(f"a∪b = {a.union(b)}", "\n")

    print(f"Дополнение а до b: {a.update(b)}")
    print(f"Дополнение а до c: {a.update(c)}", "\n")

    print(f"a\\b = {a.difference(b)}")
    print(f"a△b = {a.symmetric_difference(b)}", "\n")

    print(f"Обработка исключения (h - не множество) a∩h = {a.intersection(h)}")
