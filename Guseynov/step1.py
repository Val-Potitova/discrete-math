class Set:
    def __init__(self, lst_of_items):
        self._list = []
        for item in lst_of_items:
            self.add(item)

    def __str__(self):
        return str(" ".join(map(str, self._list)))

    def __iter__(self):
        return iter(self._list.copy())

    def add(self, item):
        if item not in self._list:
            self._list.append(item)

    def remove(self, item):
        self._list.remove(item)

    def union(set1, set2):
        return Set((set1._list + set2._list))

    def intersection(set1, set2):
        return Set([item for item in set2._list if item in set1._list])

    def difference(set1, set2):
        return Set([item for item in set1._list if item not in set2._list])

    def addiction(set1, set2):
        return Set.difference(set2, set1)


if __name__ == '__main__':
    print("	☆*:.｡.o(≧▽≦)o.｡.:*☆")
    n = input()
    set1 = Set(list(map(int, input().split())))
    set2 = Set(list(map(int, input().split())))
    operation = input()
    if operation == "u":
        print(Set.union(set1, set2))
    elif operation == "p":
        print(Set.intersection(set1, set2))
    elif operation == "-":
        print(Set.difference(set1, set2))
    elif operation == "a":
        print(Set.addiction(set1, set2))
    else:
        print(">.<")
