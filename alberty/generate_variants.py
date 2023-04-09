import random
import string

import solution
import re


open_key = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
open_key = open_key.upper()
private_key = "КФЭНИЬСЯАТУБЫЛРВЩГЪДЕМЙЦПЧЖЮШЗОХ"
file_path = 'text.txt'


def divide_text_ny_variants(length: int = 7) -> list:
    vars = []

    with open(file_path, 'r') as file:
        text = file.read()
        text = text.upper()
        text = re.split(r'[ ,:;\n]', text)
        text = list(filter(lambda a: a != '', text))
        for i in range(0, len(text)-len(text) % length, length):
            vars.append(' '.join(text[i:i+length]))

    return vars


def create_vars_and_write_to_file(file_name: str, vars: list, vars_number: int = 90) -> list:
    answers = []
    with open(file_name, 'w') as file:
        for i in range(vars_number):
            file.write(f"Вариант {i+1}.\n")

            file.write("Режим 1.\n")
            text_1 = solution.encript_mode_1(vars[i*5+1], open_key, private_key)
            file.write(f'{text_1}\n')
            answers.append(vars[i*5+1])

            file.write("Режим 2.\n")
            text_2 = solution.encript_mode_2(vars[i*5+2], open_key, private_key)
            file.write(f'{text_2}\n')
            answers.append(vars[i * 5 + 2])

            file.write("Режим 3.\n")
            ind_letter = random.choice(open_key)
            file.write(f"Индикаторная буква: {ind_letter}\n")
            text_3 = solution.encript_mode_3(vars[i * 5 + 3], open_key, private_key, ind_letter)
            file.write(f'{text_3}\n')
            answers.append(vars[i * 5 + 3])

            file.write("Режим 4.\n")
            shift = int(random.choice('4567'))
            text_4 = solution.encript_mode_4(vars[i * 5 + 4], open_key, private_key, shift)
            file.write(f'{text_4}\n')
            answers.append(vars[i * 5 + 4])

            file.write("Режим 5.\n")
            for j in vars[i * 5 + 5].split():
                if (len(j) >= 7) and bool(j.isalpha()):
                    password = j
            file.write(f"Пароль: {password}\n")
            text_5 = solution.encript_mode_5(vars[i * 5 + 5], open_key, private_key, password)
            file.write(f'{text_5}\n')
            answers.append(vars[i * 5 + 5])
    return answers


def write_answers(answers: list, file_name: str):
    with open(file_name, 'w') as file:
        for i in range(len(answers)):
            if i % 5 == 0:
                file.write(f'Вариант {i//5 + 1}.\n')
            file.write(f'Режим {i % 5 + 1}.\n')
            file.write(f'{answers[i]}\n')




def main():
    vars = divide_text_ny_variants()
    file_name = 'result.txt'
    file_for_answers = 'answers.txt'
    vars_number = 90
    answers = create_vars_and_write_to_file(file_name, vars, vars_number)
    write_answers(answers, file_for_answers)


if __name__ == '__main__':
    main()