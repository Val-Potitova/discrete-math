# Генератор булеана для множества A

len_A = int(input())
A = list(map(int, input().split()))

subs = []
for i in range(2 ** len(A)):
    subs.append((bin(i)[2:]).zfill(len(A)))

subsets = []
for i in subs:
    sub = []
    for j in range(len(A)):
        if i[j] == '1':
            sub.append(A[j])
    subsets.append(sub)

if len(A) == len_A:
    print(sorted(subsets, key=len))
else:
    print(f'Длина множества {A} не совпадает с заявленной - {len_A}.')
