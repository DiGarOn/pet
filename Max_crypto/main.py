import random
from math import gcd


def generate_phi_n(n: int):
    res = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            res.append(i)
    return res


def get_d_by_e(e: int, phi_n: list):
    for i in phi_n:
        if (e * i) % len(phi_n) == 1:
            return i


def encrypt(text: str):
    l = list(text)
    l = [ord(i) for i in l]
    # keys
    p, q = 11, 19
    n = p * q
    phi_n = generate_phi_n((p-1)*(q-1))
    e = random.choice(phi_n[1:])
    d = get_d_by_e(e, phi_n)
    print('d: ', d, 'e: ', e, 'p: ', p, 'q: ', q)
    x = random.choice([i for i in range(2, n)])
    y = (x*x)%n

    res = []
    for i in l:
        c = (i**x) % n
        r = (y**e) % n
        res.append(c)

    return res


def solve(y, n):
    res = []
    for x in range(n):
        if y%n == (x*x)%n:
            res.append(x)
    return res


def inv_solves(s: list, n):
    res = []
    for i in s:
        for j in range(n):
            if (i*j)%n == 1:
                res.append(j)
    return res


def decrypt(text: list):
    p, q = 11, 19
    n = p * q
    d = 43
    y = (text[0][1] ** d) % n
    solves = solve(y, n)
    print(solves)
    for i in text:
        inv_solves_ = inv_solves(solves, n)
        print(inv_solves_)
        for j in inv_solves_:
            print(chr((i[0]**j)%n), end="")
        print()


def main():
    text1 = 'Отмечается тенденция к увеличению в зарубежных средствах массовой информации объема материалов, содержащих предвзятую оценку государственной политики Российской Федерации. Российские средства массовой информации зачастую подвергаются за рубежом откровенной дискриминации, российским журналистам создаются препятствия для осуществления их профессиональной деятельности'
    print(text1)
    print(encrypt(text1))
    print('_____________________________')
    text2 = 'Основанная в 1927 году под названием "Легион Архангела Михаила" и организованная в военизированные отряды, "Железная гвардия" вскоре стала массовым политическим движением. Официально она была распущена в 1933-м, но продолжала функционировать и вышла на третье место по числу голосов на выборах 1937-го года. В середине 1930-х годов "Железная гвардия" установила связи с нацистским режимом в Германии.'
    print(text2)
    print(encrypt(text2))
    print('_____________________________')
    text3 = 'Следует признать, что Адольф Гитлер, неоднократно заявлявший, что ведет эту войну в качестве не только фюрера немецкого народа, но и как вождь объединенной Европы, сплотившейся вокруг него против «русских варваров», был в значительной степени прав. Красная Армия разгромила не только Германию, а всю объединенную идеями фашизма Гитлером Европу.'
    print(text3)
    print(encrypt(text3))
    print('_____________________________')


if __name__ == '__main__':
    main()
