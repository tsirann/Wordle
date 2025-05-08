from random import choice

# Присваиваем в переменную все 5 буквенные слова
with open('words5.txt', 'r', encoding='utf-8') as file:
    words_list = file.readlines()

# Проверка совпадений букв с загаданным словом
def word_exam(word) -> str:
    ls = []
    for i in range(5):
        if word[i] == correct_word[i]:
            ls.append(f'\033[32m{word[i]}')
        elif word[i] in correct_word:
            ls.append(f'\033[33m{word[i]}')
        else:
            ls.append(f'\033[37m{word[i]}')
    return ' '.join(ls) + '\033[37m'

# Основной модуль игры
def wordle_game() -> bool:
    input_list = ['□ □ □ □ □' for _ in range(6)]
    # Присваиваем переменной рандомное слово, которое нужно будет отгадать
    global correct_word
    correct_word = (choice(words_list)).rstrip()

    # Цикл обрабатывающий все 6 попыток ввода
    for i in range(6):

        print(' \033[37mWordle')
        print(*input_list, sep='\n')
        print('''\033[31mПодсказка: \033[37mA - буквы нет в слове; \033[33mА \033[37m- буква есть в слове, но не на своем месте; \033[32mА \033[37m- буква есть в слове и на своем месте.
\033[36mВведите слово:\033[37m''')

        # c - вспомогательная переменная, цикл пока не будет введено подходящее слово
        c = 0
        while c == 0:
            word_input = input().lower()
            if word_input.isalpha() and len(word_input) == 5 and (word_input + '\n') in words_list:
                input_list[i] = word_exam(word_input)
                c = 1
            else:
                print('Неизвестное слово! Попробуйте еще раз:')

        # Проверка на соответсвие слова с загаданным
        if word_input == correct_word:
            print(' \033[37mWordle')
            print(*input_list, sep='\n')
            print('''\033[32mВы победили!\033[37m
Хотите сыграть еще раз? Y/N: ''')
            if input() == 'N':
                return False
            return True

    # Если цикл не вернул ничего, значит игрок не отгадал слово и тем самым проиграл
    else:
        print(' \033[37mWordle')
        print(*input_list, sep='\n')
        print(f'''\033[31mВы проиграли!\033[37m
Загаданное слово: {correct_word}
Хотите сыграть еще раз? Y/N: ''')
        if input() == 'N':
            return False
        return True

# Цикл для повторения игр и для ее запуска
while True:
    if not wordle_game():
        break