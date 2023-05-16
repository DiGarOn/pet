import random
import string

import solution
import re


open_key = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
open_key = open_key.upper()
private_key = "КФЭНИЬСЯАТУБЫЛРВЩГЪДЕМЙЦПЧЖЮШЗОХ"
file_path = 'text.txt'


def divide_text_ny_variants(length: int = 4) -> list:
    vars = []

    with open(file_path, 'r') as file:
        text = file.read()
        text = text.upper()
        text = re.split(r'[ ,:;\n]', text)
        text = list(filter(lambda a: a != '', text))
        for i in range(0, len(text)-len(text) % length, length):
            if len(' '.join(text[i:i+length])) < 50:
                vars.append(' '.join(text[i:i+length]))

    return vars


def create_vars_and_write_to_file(file_name: str, vars: list, vars_number: int = 90) -> list:
    answers = []
    with open(file_name, 'a') as file:
        file.write("\\textbf{\\textit{Ключ к расшифрованияю:} К\,\, Ф \,\,Э\,\, Н\,\, И\,\, Ь\,\, С\,\, Я\,\, А\,\, Т\,\, У\,\, Б\,\, Ы\,\, Л\,\, Р\,\, В\,\, Щ\,\, Г\,\, Ъ\,\, Д\,\, Е\,\, М\,\, Й\,\, Ц\,\, П\,\, Ч\,\, Ж\,\, Ю\,\, Ш\,\, З\,\, О\,\, Х\,\,}")
        for i in range(vars_number):
            file.write("\\begin{exercise}")

            file.write("\\begin{table}[H]\n"
                       "\t\centering\n"
                       "\t\\begin{tabular}{r l}")

            file.write("\\textbf{Режим 1}  ")
            text_1 = solution.encript_mode_1(vars[i*5+1], open_key, private_key)
            file.write(f'& {text_1} \\\ \n')
            answers.append(vars[i*5+1])

            file.write("\\textbf{Режим 2}  ")
            text_2 = solution.encript_mode_2(vars[i*5+2], open_key, private_key)
            file.write(f'& {text_2} \\\ \n')
            answers.append(vars[i * 5 + 2])

            file.write("\\textbf{Режим 3}  ")
            ind_letter = random.choice(open_key)
            file.write(f"& Индикаторная буква: {ind_letter} \\\ \n")
            text_3 = solution.encript_mode_3(vars[i * 5 + 3], open_key, private_key, ind_letter)
            file.write(f'& {text_3} \\\ \n')
            answers.append(vars[i * 5 + 3])

            file.write("\\textbf{Режим 4}  ")
            shift = int(random.choice('4567'))
            text_4 = solution.encript_mode_4(vars[i * 5 + 4], open_key, private_key, shift)
            file.write(f'& {text_4} \\\ \n')
            answers.append(vars[i * 5 + 4])

            file.write("\\textbf{Режим 5}  ")
            for j in vars[i * 5 + 5].split():
                if (len(j) >= 7) and bool(j.isalpha()):
                    password = j
            file.write(f"& Пароль: {password} \\\ \n")
            text_5 = solution.encript_mode_5(vars[i * 5 + 5], open_key, private_key, password)
            file.write(f'& {text_5} \\\ \n')
            answers.append(vars[i * 5 + 5])

            file.write("\t\end{tabular} \n"
                       "\end{table}\n\n"
                       "\end{exercise}\n")

            file.write("\\begin{solution}\n")

            file.write("\\begin{table}[H]\n"
                      "\t\centering\n"
                      "\t\\begin{tabular}{r l}")


            file.write("\\textbf{Режим 1}  ")
            file.write(f'& {vars[i * 5 + 1]} \\\ \n')

            file.write("\\textbf{Режим 2}  ")
            file.write(f'& {vars[i * 5 + 2]} \\\ \n')

            file.write("\\textbf{Режим 2}  ")
            file.write(f"& Индикаторная буква: {ind_letter} \\\ \n")
            file.write(f'& {vars[i * 5 + 3]} \\\ \n')

            file.write("\\textbf{Режим 4}  ")
            file.write(f'& {vars[i * 5 + 4]} \\\ \n')

            file.write("\\textbf{Режим 5}  ")
            file.write(f"& Пароль: {password} \\\ \n")
            file.write(f'& {vars[i * 5 + 5]} \\\ \n')

            file.write("\t\end{tabular} \n"
                       "\end{table}\n\n"
                       "\end{solution}\n")


        file.write("\end{document}")

    return answers


def write_answers(answers: list, file_name: str):
    with open(file_name, 'w') as file:
        for i in range(len(answers)):
            if i % 5 == 0:
                file.write(f'Вариант {i//5 + 1}.\n')
            file.write(f'Режим {i % 5 + 1}.\n')
            file.write(f'{answers[i]}\n')


def write_skeleton(skeleton: str, file_name:str):
    with open(file_name, 'w') as file, open(skeleton, 'r') as scull:
        for line in scull:
            if line == '\\begin{exercise}\n':
                return
            file.write(line)


def main():
    vars = divide_text_ny_variants()
    file_variants = 'variants.tex'
    # file_for_answers = 'answers.tex'
    skeleton_path = 'alberti_skeleton.tex'

    vars_number = 90
    # print(len("ЙАГЬММУ ВФИВЫФЪХСКЙ ОЭАФЭЗЩЬЙЮЧППЪ ТЫЛДДНДРРЩЩЬ"))
    write_skeleton(skeleton_path, file_variants)
    # write_skeleton(skeleton_path, file_for_answers)
    answers = create_vars_and_write_to_file(file_variants, vars, vars_number)
    # write_answers(answers, file_for_answers)


if __name__ == '__main__':
    main()