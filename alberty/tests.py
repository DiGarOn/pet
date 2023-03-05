import solution
import random

open_key = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
open_key = open_key.upper()
private_key = "КФЭНИЬСЯАТУБЫЛРВЩГЪДЕМЙЦПЧЖЮШЗОХ"

for i in range(100):
    text_length = 40
    password_length = 10
    shift = 7
    text = (''.join(random.choices(private_key, k=text_length)))
    ind = str(random.choice(private_key)).upper()
    password = (''.join(random.choices(private_key, k=password_length)))

    enc_text_1 = solution.encript_mode_1(text, open_key, private_key)
    if solution.decript(enc_text_1, open_key, private_key, 1) != text:
        print("wrong in 1")
        print(text)
        break

    enc_text_2 = solution.encript_mode_2(text, open_key, private_key)
    if text not in solution.decript_mode_2(enc_text_2, open_key, private_key):
        print("wrong in 2")
        print(text)
        break

    enc_text_3 = solution.encript_mode_3(text, open_key, private_key, ind)
    if text != solution.decript_mode_3(enc_text_3, open_key, private_key, ind):
        print("wrong in 3")
        print(text)
        break

    enc_text_4 = solution.encript_mode_4(text, open_key, private_key, shift)
    if text != solution.decript_mode_4(enc_text_4, open_key, private_key, shift):
        print("wrong in 4")
        print(text)
        print(enc_text_4)
        print(solution.decript_mode_4(enc_text_4, open_key, private_key, shift))
        break

    enc_text_5 = solution.encript_mode_5(text, open_key, private_key, password)
    if text != solution.decript_mode_5(enc_text_5, open_key, private_key, password):
        print("wrong in 5")
        print(text)
        break

print('Everything is correct!')
