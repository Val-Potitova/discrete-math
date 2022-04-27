# Операции с множествами A и B
# объединятор(u), пересекатор(i или p), вычитатор(s или -) и дополнятор(a)

while True:
    len_A, len_B = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    operation = input()

    if len(A) != len_A:
        print(f'Длина множества {A} не совпадает с заявленной - {len_A}.')
    elif len(B) != len_B:
        print(f'Длина множества {B} не совпадает с заявленной - {len_B}.')
    elif operation == 'u':
        print(A.union(B))
    elif operation == 'i' or operation == 'p':
        print(A.intersection(B))
    elif operation == 's' or operation == '-':
        print(A.difference(B))
    elif operation == 'a':
        print(B.difference(A))
    else:
        print(f'Операции {operation} не существует!')
