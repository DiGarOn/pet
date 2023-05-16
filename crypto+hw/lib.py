import re


# транспозиция букв слов
def transposeText(text):
    transposedText = []
    for word in text.split():
        transposed = ""
        for i in range(0, len(word), 2):
            if i + 1 < len(word):
                transposed += word[i + 1] + word[i]
            else:
                transposed += word[i]
        transposedText.append(transposed)
    return transposedText


# подготавливаем текст
def prepareText(text):
    text = text.lower()
    text = text.replace('й', 'и')
    text = text.replace('ё', 'е')
    text = re.sub(r'[^\w\s]', '', text)
    return ' '.join(transposeText(text))


# шифруем текст
def encrypt(text, key, codeDict):
    encryptedText = []
    for index, symbol in enumerate(text):
        encryptedText.append(codeDict[symbol] ^ codeDict[key[index % len(key)]])
    return encryptedText


# дешифруем текст
def decrypt(encryptedText, key, letterDict):
    decryptedText = []
    for index, symbol in enumerate(encryptedText):
        decryptedText.append(symbol ^ codeDict[key[index % len(key)]])
    return decryptedText


# перевод десятичных чисел в двоичные для просмотра
def decTextToBin(decText):
    return ["%05d" % int(bin(symbol)[2:]) for symbol in decText]


def decTextToStr(decText, letterDict, isTransposed=True):
    text = ''.join(letterDict[symbol] for symbol in decText)
    if not isTransposed:
        return ' '.join(transposeText(text))
    return text

# задаем словари для преобразования букв в коды и наоборот
alphabet = 'абвгдежзиклмнопрстуфхцчшщъыьэюя '
codeDict = {let: alphabet.index(let) for let in alphabet}
letterDict = {i: alphabet[i] for i in range(len(alphabet))}
text = prepareText('Отмечается тенденция к увеличению в зарубежных средствах массовой информации объема материалов, содержащих предвзятую оценку государственной политики Российской Федерации. Российские средства массовой информации зачастую подвергаются за рубежом откровенной дискриминации, российским журналистам создаются препятствия для осуществления их профессиональной деятельности')
key = 'вшэ'
encryptedText = encrypt(text, key, codeDict)
print(decTextToStr(encryptedText, letterDict))
print(decTextToStr(encryptedText, letterDict) == "фыъкшлфувуиъффспухшкгмиясюъх сзлхюцгвспоуюптищифуфъфзэаггвэнуцтлыгп ттэфшшхлиюруевэгвэъф фишяритуущдщдвгхющужуьажв егшысзецюы сзэжзфажсзыслитн члжхмитознл цу тюурзфэо клитознл цуухющнжуоушяюшшузяр тюьхрдшовэл гвсэхжн егръяжщъвхо кнюшьюефзчтдэгфыфмцтпутп глфцу флээп клитознл цуэхюеыпщчвзхвжшюынжсбвзоэифнъъфкоу яэичжкгуыдсзъажъи сэиилифндтуухуьтишсъ тюущфкчзьзуыхф")