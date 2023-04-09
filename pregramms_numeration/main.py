from functools import cmp_to_key


def self_comp(l1, l2):
    if sum(l1) > sum(l2):
        return 1
    if sum(l1) < sum(l2):
        return -1
    for i in range(len(l1)):
        if l1[i] > l2[i]:
            return 1
        if l1[i] < l2[i]:
            return -1
    return 0


def self_sor(l: list):
    return sorted(l, key = cmp_to_key(self_comp))


def generate_len_1(v: int):
    res = [v]

    return res


def generate_len_2(v: int):
    res = []

    for value in range(2, v):
        for comb in generate_combinations(2, value):
            res.append(comb)

    return self_sor(res)


def generate_len_3(v: int):
    res = []

    for value in range(3, v):
        for comb in generate_combinations(3, value):
            res.append(comb)

    return self_sor(res)


def generate_combinations(length, total_sum):
    if length == 1:
        yield [total_sum]
    else:
        for value in range(1, total_sum):
            for combination in generate_combinations(length - 1, total_sum - value):
                yield [value] + combination


def generate(n: int):
    res = []

    for length in range(1, n):
        for value in range(length, n):
            for comb in generate_combinations(length, value):
                res.append(comb)

    return self_sor(res)


def main():
    print("набор команд по номеру программы:")
    m = generate(7)
    for i in range(len(m)):
        print(i+1, m[i])

    print("параметры команды от 3х:")
    m = generate_len_3(7)
    for i in range(len(m)):
        print(i + 1, m[i])

    print("параметры команды от 2х:")
    m = generate_len_2(7)
    for i in range(len(m)):
        print(i + 1, m[i])


if __name__ == '__main__':
    main()
