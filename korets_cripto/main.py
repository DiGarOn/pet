

text1= 'Отмечается тенденция к увеличению в зарубежных средствах массовой информации объема материалов, ' \
       'содержащих предвзятую оценку государственной политики Российской Федерации. Российские средства массовой ' \
       'информации зачастую подвергаются за рубежом откровенной дискриминации, российским журналистам ' \
       'создаются препятствия для осуществления их профессиональной деятельности'

text2="Если тебе тяжело, значит ты поднимаешься в гору. Если тебе легко, значит ты летишь в пропасть."

text3="Молчание и улыбка — это два мощных оружия. Улыбка является способом решения многих проблем, молчание же помогает их избежать."

text4="Слишком много людей ломается, даже не зная, как близко к успеху они были в тот момент, когда упали духом."




def split_by_8(s: str):
    res = []
    for i in range(0, len(s), 8):
        res.append(s[i:i+8])
    return res


def replace_letters(s: str, key: list):
    res = ''
    for i in key:
        res += s[i]
    return res


def str_to_bites(s: str):
    res = ''
    for i in s:
        tmp = str("{0:b}".format(ord(i)))
        while len(tmp) != 12: # !
            tmp = '0' + tmp
        res += tmp
    return res


def rotate_left(private_key):
    return private_key[1: ] + private_key[: 1]


def make_key(s: str, text: str):
    res = ''
    res += s
    tmp = rotate_left(s)
    while len(res) < len(text):
        res += tmp
        tmp = rotate_left(tmp)
    while len(res) > len(text):
        res = res[:-1]
    return res


def xor(text: str, key: str):
    res = ''
    for i in range(len(text)):
        res += str(int(text[i:i+1])^int(key[i:i+1]))
    return res


def bites_to_str(s: str):
    res = ''
    for i in range(0, len(s), 12):
        res += chr(int(s[i: i+12], 2))
    return res


def encrypt(s: str):
    while len(s) % 8 != 0:
        s += " "
    s_list = split_by_8(s)
    # print("1", s_list)
    # print('1.1', str_to_bites(s_list[0]))
    key_0 = [2, 3, 6, 5, 1, 0, 7, 4]
    stroka = ''
    for i in s_list:
        stroka += replace_letters(i, key_0)
    prom_s = str_to_bites(stroka)
    # print("2", prom_s)
    key_1 = '11110000101010' # 14
    key_1 = make_key(key_1, prom_s)
    enc_bites = xor(prom_s, key_1)
    # print("3", enc_bites)
    enc_text = bites_to_str(enc_bites)
    l = []
    for i in enc_text:
        l.append(ord(i))
    return l


def reverce_replace(s: str, key: list):
    res = ''
    for i in range(8):
        res += s[key.index(i)]
    return res


def decrypt(l: list):
    s = ''
    for i in l:
        s += chr(i)
    prom_s = str_to_bites(s)
    # print('2', prom_s)
    key_1 = '11110000101010'  # 14
    key_1 = make_key(key_1, prom_s)
    enc_bites = xor(prom_s, key_1)
    s = bites_to_str(enc_bites)
    s_list = split_by_8(s)
    # print('1', s_list)
    # print('1.1', str_to_bites(s_list[0]))
    key_0 = [2, 3, 6, 5, 1, 0, 7, 4]
    stroka = ''
    for i in s_list:
        stroka += reverce_replace(i, key_0)
    # print('1.1',stroka)

    return stroka


text = 'aaaa'

enc_text = encrypt(text1)
print(enc_text)
print("____________________________________")
print(decrypt(enc_text))