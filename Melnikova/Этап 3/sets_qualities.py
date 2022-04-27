def reflexivity(ex_vertices, ex_pairs):
    ref_vertices = []
    count = 0
    for i in ex_vertices:
        ref_vertices.append([i, i])
    for i in ref_vertices:
        if i in ex_pairs:
            count += 1

    if count == len(ex_vertices):
        return "рефлексивно"
    elif count == 0:
        return "антирефлексивно"
    else:
        return "нерефлексивно"


def symmetry(ex_vertices, ex_pairs):
    sym_pairs = []
    for i in ex_pairs:
        sym_pairs.append([i[1], i[0]])

    if sorted(sym_pairs) == sorted(ex_pairs):
        a = "симметрично"
    else:
        count_sym_pairs = 0
        count_not_sym_pairs = 0

        for i in sym_pairs:
            if i in ex_pairs:
                if i[0] == i[1]:
                    count_sym_pairs += 1
                else:
                    count_not_sym_pairs += 1

        if count_sym_pairs != 0 and count_not_sym_pairs == 0:
            a = "антисимметрично"
        elif count_not_sym_pairs != 0:
            a = "НЕ симметрично, НЕ асимметрично, НЕ антисимметрично"
        else:
            a = "асимметрично"
    return a


def is_transitive(ex_pairs):
  second_element = []
  for (a, b) in ex_pairs:
    second_element.append(b)
    for (a, b) in ex_pairs:
        for c in second_element:
            if (b, c) in ex_pairs and (a, c) not in ex_pairs:
                return "не транзитивно"
    return "транзитивно"


vertices, edges = map(int, input().split())

existing_vertices = []
for i in range(vertices):
  existing_vertices.append(i)

existing_pairs = []
for i in range(edges):
  existing_pairs.append(list(map(int, input().split())))

if __name__=='__main__':
    print(reflexivity(existing_vertices, existing_pairs))
    print(symmetry(existing_vertices, existing_pairs))
    print(is_transitive(existing_pairs))
