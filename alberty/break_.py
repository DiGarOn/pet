import solution

open_key = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
open_key = open_key.upper()
private_key = "КФЭНИЬСЯАТУБЫЛРВЩГЪДЕМЙЦПЧЖЮШЗОХ"

text_1 = "В ОЩ ЖШЪВ, БЙВБ ИГКЬНРСТСЫ ЮЬЯАПДЭЭЭГФ"
text_2 = "Ы НЛЗФХБЬ, ТЮС УУЬФГ ЖП ОЧЮУЦ ОЯП,"
text_3 = "ЛЩЛЛЙ ЬЗЯАЦЭП ЕХФЧОЪЗПВЮ ЦЫЦЪЪЪЯРШИ,"
ind = "О"
text_4 = "ЦфцфхнЧяжтчкЕэкйэхЬунлщлЗуэхбаФсходтКбоиа"
password  = "Перестановка".upper()
text_5 = "П ФТФБ ППАЭ ФРТСЗ, КЭЦДЙЫ ЗЙЭЩИ,"

# print(solution.decript(text_1, open_key,private_key, 1))
# print(solution.decript_mode_2(text_2, open_key, private_key))
# print(solution.decript_mode_3(text_3, open_key, private_key, ind))
# print(solution.decript_mode_4(text_4, open_key, private_key, 5))
print(solution.decript_mode_5(text_5, open_key, private_key, password))