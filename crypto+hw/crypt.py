import nltk
from nltk.corpus import wordnet
nltk.download('omw-1.4')


alpho = 'абвгдежзиклмнопрстуфхцчшщъыьэюя '


def trans(text: str) -> str:
    res = ''
    for j in text.split():
        for i in range(0, len(j), 2):
            res += j[i:i+2][::-1]
        res += " "

    res = res[:-1]
    return res


def encrypt(text: str, key: str) -> str:
    global alpho

    res = ''
    t = text.lower()
    t = t.replace('й', 'и')
    t = t.replace('ё', 'е')
    t = t.replace(',', '')
    t = t.replace('.', '')
    t = trans(t)

    for i in range(len(t)):
        a = alpho.find(t[i])
        b = alpho.find(key[i%len(key)])
        c = a^b
        res += alpho[c]

    return res


def decrypt(text: str, key: str) -> str:
    global alpho

    res = ''
    for i in range(len(text)):
        a = alpho.find(text[i])
        b = alpho.find(key[i%len(key)])
        c = a^b
        res += alpho[c]

    t = trans(res)

    return t



text = "Отмечается тенденция к увеличению в зарубежных средствах массовой информации объема материалов, содержащих предвзятую оценку государственной политики Российской Федерации. Российские средства массовой информации зачастую подвергаются за рубежом откровенной дискриминации, российским журналистам создаются препятствия для осуществления их профессиональной деятельности"
key = "вшэ"
enc =   "фыъкшлфувуиъффспухшкгмиясюъх сзлхюцгвспоуюптищифуфъфзэаггвэнуцтлыгп ттэфшшхлиюруевэгвэъф фишяритуущдщдвгхющужуьажв егшысзецюы сзэжзфажсзыслитн члжхмитознл цу тюурзфэо клитознл цуухющнжуоушяюшшузяр тюьхрдшовэл гвсэхжн егръяжщъвхо кнюшьюефзчтдэгфыфмцтпутп глфцу флээп клитознл цуэхюеыпщчвзхвжшюынжсбвзоэифнъъфкоу яэичжкгуыдсзъажъи сэиилифндтуухуьтишсъ тюущфкчзьзуыхф"
enc_text = encrypt(text, key)
dec_text = decrypt(enc, key)
# print(dec_text)


def generate_key():
    global alpho
    keys = []
    for i in alpho:
        for j in alpho:
            for k in alpho:
                keys.append(i + j+ k)

    return keys


def break_shipher(text):
    keys = generate_key()
    print(wordnet.langs())
    # print(nltk.sent_tokenize(text, language="russian"))
    for key in keys:
        tmp = decrypt(text, key)
        if wordnet.synsets(tmp.split()[0], lang='rus'):
            print(tmp, key)

break_shipher(enc)
