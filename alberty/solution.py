import random


# open_key = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
# open_key = open_key.upper()
# private_key = "КФЭНИЬСЯАТУБЫЛРВЩГЪДЕМЙЦПЧЖЮШЗОХ"
#
# text1_1 = "ТГСДУЖ ШМФ ПЮШЧМГ, ЪМЙДВАИШ А РЫАСТШЯШЛГ"
# text1_1_1 = 'ТЫСЯЧИ ЛЕТ КОРОЛИ, КОРОЛЕВЫ И ПОЛКОВОДЦЫ'
#
# text1_2 = "ФВ Ч КЕЮВХМП ШПДПЭПДТ ТЯЫКЫЖЭ."
# text1_2_1 = 'МЫ Ж ОГЛАСИМ СОКРЫТОЕ ЖЕЛАНЬЕ.'
#
# text1_3 = 'МЮР ЧКННЪО УМУ ЕЪЯШСЫУЗ ЫШБЛУ ЬЪНЖ,'
# ind_1 = 'Г'
# text_1_3_1 = 'ДЛЯ ЛУЧШИХ ВОД ПОДЪЕМЛЯ ПАРУС НЫНЕ,'
#
# text1_4 = 'ЧсонябЖауахшРоджлкЯмджеяЩцщегкУушшыпТъдцчцТеь'
# text1_4_1 = 'НЕКОТОРОЕВРЕМЯТОМУНАЗАДБРАТТВОЙКОРОЛЬ'
#
# text1_5 = 'НСБЕ Н ЕТКБ, ЙСЕЬ, ЩЗИС ЖЪ ЪАНН,'
# password = 'Подпись'.upper()
# text1_5_1 = 'ЛИШЬ Я ОДИН, ГОРЯ, ЛЕЖУ ВО МГЛЕ,'


def rotate_for(private_key, n = 1):
    return (private_key[len(private_key)-n:] + private_key)[:32]


def rotate_up(private_key, n = 1):
    return private_key[n: ] + private_key[: n]


def decript_mode_2(text, open_key, private_key):
    res = []
    for i in range(32):
        res.append(decript(text, open_key, private_key, 2))
        open_key = rotate_for(open_key)
    return res


def decript(text, open_key, private_key, mode):
    res = ""
    if mode == 1:
        while open_key[0] != text[0]:
            open_key = rotate_for(open_key)
        while private_key[0] != text[0]:
            private_key = rotate_for(private_key)
    else:
        pass

    for letter in text:
        if letter in open_key:
            res += open_key[private_key.find(letter)]
            private_key = rotate_for(private_key)
        else:
            res += letter
    return res


def decript_mode_3(text, open_key, private_key, ind):
    while private_key[0] != ind:
        private_key = rotate_for(private_key)
    return decript(text, open_key, private_key, 2)


def decript_mode_4(text, open_key, private_key, shift):
    res = ''
    i = 0
    while i < len(text):
        while private_key[0] != text[i]:
            private_key = rotate_for(private_key)
        sub_terxt = text[i + 1: i + shift + 1].upper()
        for letter in sub_terxt:
            res += open_key[private_key.find(letter)]
        i += shift + 1
    return res


def decript_mode_5(text, open_key, private_key, password):
    res = ''
    i = 0
    j = i
    while i < len(text):
        if (text[i] in private_key):
            while private_key[0] != password[j % len(password)]:
                private_key = rotate_for(private_key)
            res += open_key[private_key.find(text[i])]
            j += 1
        else:
            res += text[i]
        i += 1
    return res


def encript_mode_1(text, open_key, private_key, rotate_value = 1):
    while private_key[0] != text[0]:
        private_key = rotate_for(private_key)
    while open_key[0] != text[0]:
        open_key = rotate_for(open_key)
    res = ''
    for letter in text:
        if (letter in private_key):
            res += private_key[open_key.find(letter)]
            private_key = rotate_for(private_key)
        else:
            res += letter
    return res


def encript_mode_2(text, open_key, private_key):
    while private_key[0] != text[0]:
        private_key = rotate_for(private_key)
    res = ''
    for letter in text:
        if (letter in private_key):
            res += private_key[open_key.find(letter)]
            private_key = rotate_for(private_key)
        else:
            res += letter
    return res


def encript_mode_3(text, open_key, private_key, ind):
    while private_key[0] != ind:
        private_key = rotate_for(private_key)
    res = ''
    for letter in text:
        if (letter in private_key):
            res += private_key[open_key.find(letter)]
            private_key = rotate_for(private_key)
        else:
            res += letter
    return res


def encript_mode_4(text, open_key, private_key, shift):
    text = text.replace(' ', '')
    res = ''
    for i in range(len(text) // shift):
        key = random.choice(private_key)
        while private_key[0] != key:
            private_key = rotate_for(private_key)
        res += key
        for j in range(i * shift, i * shift + shift):
            res += private_key[open_key.find(text[j])].lower()
    if len(text) % shift != 0:
        key = random.choice(private_key)
        while private_key[0] != key:
            private_key = rotate_for(private_key)
        res += key
        for i in range(len(text) - len(text) % shift, len(text)):
            res += private_key[open_key.find(text[i])].lower()
    return res


def encript_mode_5(text, open_key, private_key, password):
    res = ''
    i = 0
    j = i
    while i < len(text):
        if (text[i] in private_key):
            while private_key[0] != password[j % len(password)]:
                private_key = rotate_for(private_key)
            res += private_key[open_key.find(text[i])]
            j += 1
        else:
            res += text[i]
        i += 1
    return res
