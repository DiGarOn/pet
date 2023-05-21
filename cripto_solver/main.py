import re
# import nltk


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


def check_words(text):
    global dictionary
    for word in text.split():
        if not(dictionary.check(word)):
            return False
    return True


# def break_(encText):
#     global alphabet
#     global letterDict
#     key = ''
#     for i in range(len(alphabet)):
#         key = alphabet[i]
#         decText = decrypt(encText, key, letterDict)
#         if check_words(decText):
#             print(decText)
#     key = ''
#     for j in alphabet:
#         for k in alphabet:
#             key = j + k
#             decText = decrypt(encText, key, letterDict)
#             if check_words(decText):
#                 print(decText)
#     key = ''
#     for i in alphabet:
#         for j in alphabet:
#             for k in alphabet:
#                 key = i + j + k
#                 decText = decrypt(encText, key, letterDict)
#                 if check_words(decText):
#                     print(decText)


# задаем словари для преобразования букв в коды и наоборот
alphabet = 'абвгдежзиклмнопрстуфхцчшщъыьэюя '
codeDict = {let: alphabet.index(let) for let in alphabet}
letterDict = {i: alphabet[i] for i in range(len(alphabet))}
# dictionary = enchant.Dict("ru_RU")

# text = prepareText(input())
# key = 'вшэ'
# encryptedText = encrypt(text, key, codeDict)
# print(decTextToStr(encryptedText, letterDict))

# text = "дшхзшэпсююнрнабрш ифоэобущюмкююуэмюбрирфдююсдфуыл рщфрвъдпгнзгвпоюитэлуцичэсощюсъпывуоспоцшиылоцкнашопюкя" \
#        " оцкубаьывяююняпгхвуеъгрвюшюсрзчмпобхфющояуящвоцпоюгшывщржусощрфдтрирщфмфоую гсьцуоамясмуаюгжг" \
#        " люяафнмюуэоэфэо фсссьрфдтрируавпкбю ъвьэлобхфющо нвюсямфнаюырръгоящюаэю яргвкобх рп рмсасиэл"
#
# break_(text)

text = 'абабаб'
key = 'вг'

encryptedText = encrypt(text, key, codeDict)
print(encryptedText)
print(decTextToStr(encryptedText, letterDict))