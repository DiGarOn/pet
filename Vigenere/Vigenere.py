import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.corpus import words
import itertools
import math
from frases import create_phrases


alfo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

Vigenere_table = {}
for i in range(len(alfo)):
    tmp = alfo[i:] + alfo[:i]
    Vigenere_table[alfo[i]] = tmp


def get_table(alfo: str) -> dict:
    Vigenere_table = {}
    for i in range(len(alfo)):
        tmp = alfo[i:] + alfo[:i]
        Vigenere_table[alfo[i]] = tmp

    return Vigenere_table


def encrypt(text: str, key: str) -> str:
    global Vigenere_table
    global alfo
    text = text.upper()
    key = key.upper()
    res = ''

    count  = 0
    for i in range(len(text)):
        if text[i] in alfo:
            res += Vigenere_table[key[count % len(key)]][ord(text[i]) - ord('A')]
            count += 1

    return res


# text = 'ATTACKATDAWN'
# key = 'Lemon'
#
# enc_text = encrypt(text, key)


def decrypt(text: str, key: str) -> str:
    global alfo
    global Vigenere_table
    text = text.upper()
    key = key.upper()
    res = ''

    count = 0
    for i in range(len(text)):
        if text[i] in alfo:
            res += alfo[Vigenere_table[key[count%len(key)]].find(text[i])]
            count += 1
        else:
            res += text[i]

    return res


# В этой функции мы используем модуль NLTK для токенизации текста и определения синонимов для
# каждого слова в тексте с помощью WordNet. Затем мы проверяем, есть ли синонимы в тексте,
# и выводим соответствующий результат. Если синонимы были найдены в тексте, мы считаем текст
# осмысленным, в противном случае - бессмысленным.
# def check_text(text: str):
#     # Токенизация текста
#     tokens = word_tokenize(text)
#
#     # Определение синонимов для каждого слова в тексте
#     synonyms = []
#     for token in tokens:
#         for syn in wordnet.synsets(token):
#             for lemma in syn.lemmas():
#                 synonyms.append(lemma.name())
#
#     # Проверка наличия синонимов в тексте
#     if set(synonyms) & set(tokens):
#         return True
#     else:
#         return False


# def generate_keys_by_value(key_len: int):
#     global alfo
#     res = [''.join(p) for p in itertools.product(alfo, repeat=key_len)]
#
#     return res


# import nltk
# nltk.download("words")
def func(l: int):
    word_list = [word.upper() for word in words.words() if len(word) == l]
    return word_list


def f(text: str, keys: list):
    count = 0
    for i in keys:
        if i.upper() in text:
            count += 1
        if count > 7:
            return True
    return False

#
# def is_meaningful_text(text: str):
#     """
#     Функция проверяет, является ли текст, склеенный без пробелов, осмысленным.
#
#     Parameters:
#         text (str): Текст, склеенный без пробелов.
#
#     Returns:
#         bool: True, если текст является осмысленным, False в противном случае.
#     """
#
#     # Разбиваем текст на отдельные слова
#     words = nltk.word_tokenize(text)
#
#     # Выполняем морфологический анализ каждого слова
#     tagged_words = nltk.pos_tag(words)
#
#     # Проверяем, есть ли в тексте глаголы и существительные
#     has_noun = False
#     has_verb = False
#     for word, tag in tagged_words:
#         if tag.startswith('N'):
#             has_noun = True
#         elif tag.startswith('V'):
#             has_verb = True
#
#     return has_noun and has_verb


def fu(word_length: int):
    # получаем список всех синсетов (множеств слов-синонимов) для всех частей речи
    all_synsets = []
    for pos in ['n', 'v', 'a', 'r']:
        all_synsets.extend(list(wordnet.all_synsets(pos=pos)))

    # инициализируем пустой список для хранения слов фиксированной длины
    words = []

    # проходимся по каждому синсету в общем списке синсетов
    for synset in all_synsets:
        # проходимся по каждому имени (слову) в каждом синсете
        for name in synset.lemma_names():
            if len(name) == word_length and not '-' in name and not '_' in name and not '\'' in name and not '2' in name and not '.' in name and not '1' in name and not '0' in name and not name in words:  # если длина слова совпадает с заданной
                words.append(name)  # добавляем слово в список

    # выводим полученный список осмысленных слов фиксированной длины
    return words


keys = fu(5)


# def is_meaningful_text_in_(text: str):
#     count = 0
#     for i in words.words():
#         if i in text:
#             count += 1
#         if count >= 10:
#             return True
#     return False


def break_Vigenere(text: str, key_len: int) -> list:
    global alfo
    global Vigenere_table
    global keys
    text = text.upper()
    res = []

    # keys = generate_keys_by_value(key_len)
    for i in keys:
        # print(i.upper())
        tmp = decrypt(text, i.upper())
        # print(tmp)
        # print("_____________________________________________")
        if f(tmp, keys):
            res.append([tmp, i])
            print([tmp, i])

    return res


text = "AVCKKSOXWMUHBWVPBAGJAFYWWDOMWZPRYFXSMUEILHCFKWZUUIVTNZIDCFNI\
ZAIJIHBXESYSEWTAQIEMUUCFXOSSDIMHAMEYRMSXAVYXSVHIXXOSNJILWHOL\
PQBVSYWUFHIWFTSDSLWEURNZIUKYFXZBCXJSWHYEICOLXPZFLLLMBSHZAYDX\
VINWZLFSLVLSNZEAVUVEUMIFIPBCLXOSMWXOSSYYHFXWHACI"


text_1 = 'WHRPXKELYEQTRFXRKAQADLYCFRUGJMVAQXIQTHTIVASVIUTUGCKAQNSVTUKQ\
DNQJIVAGFSZNNPHWOYFXKEZGZHRLVLLNTGBFECVEEOHVXKESKRGIAISITUGV\
LNTVLHYJGVHPNTXLCHNEULLKRWEEGWWEQKRWHRTMGDYGGRMCGXLTVQRDNQUL\
XDQGVHDZQWWACRVHCVCXLVRNCDTUKWGEFEVLPGKSQOSISOLHO'


enc_text = decrypt(text, "HOUSE")

# t1 = 'HBXRMZUSDO|BNWDXWHVNL|HLTDYKUHDB|WXTMZZSPLK|SNXMMDFPBK|CZIGKKIAUK \n         GGDQKOHSLU|FYZDVHWDLO|BAXMZVYNKK|TNVTGFXHZZ|HBTEUCNDEZ|VYIQKSCCVN \n         WWWCUFCPMJ|PCAAUKYGDG|BXIGKBQTMZ|GHXELZCCFG|PIJSZWFASN|SSWZJGGTKZ \n         COIDBSLNSX|SYIGGHBPCG|BSDMKWHXSZ|VYHDZVYNFA|OLSDJHID'

# print(f(enc_text, keys))
# print("shark" in keys)
# print(is_meaningful_text_in_(text))
# print(keys)
print(break_Vigenere(text_1, 5))
# print(f(enc_text))
#
# phr = create_phrases()
#
# for i in phr:
#     print(len(i))
#
# text = 'HUIDSHEUUYMBXBZVRHFWQGPCPWRNVAIYHVBPXCUJIJQOAXTTDXKRYBBAFVLXVBPVSBZAAQSBXBQSRTTPEBLRRXPAGFPBKABJBLQIGRWFGSFVPQKLCSFBZVGKBDBRPDZESHUMYGPPHVFXGJGNFSSSAVQWCQRSUNMZ'
#
# for i in phr:
#     tmp = decrypt(text, i)
#     if f(tmp, keys):
#         print([tmp, i])
