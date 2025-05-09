from random import choice

# Присваиваем переменной список пятибуквенных слов
with open('words5.txt', 'r', encoding='utf-8') as file:
    words_list = [word.rstrip() for word in file.readlines()]

# Цвета
green = '\033[32m'
yellow = '\033[33m'
white = '\033[37m'
red = '\033[31m'
blue = '\033[36m'

def word_exam(word, correct_word) -> str:
    """Проверяет слово на совпадения букв и возвращает раскрашенное слово"""
    colored_letters = []
    for i in range(5):
        if word[i] == correct_word[i]:
            colored_letters.append(green + word[i])
        elif word[i] in correct_word:
            colored_letters.append(yellow + word[i])
        else:
            colored_letters.append(white + word[i])
    return ' '.join(colored_letters) + white

def wordle_game() -> bool:
    """Основной цикл игры Wordle"""
    input_list = ['□ □ □ □ □' for _ in range(6)]
    correct_word = (choice(words_list)).rstrip() # Присваиваем переменной рандомное слово, которое нужно будет отгадать

    # Цикл обрабатывающий все 6 попыток ввода
    for i in range(6):

        print(f' {white}Wordle')
        print(*input_list, sep='\n')
        print(f'''{red}Подсказка: {white}A - буквы нет в слове; {yellow}А {white}- буква есть в слове, но не на своем месте; {green}А {white}- буква есть в слове и на своем месте.
{blue}Введите слово:{white}''')

        # c - вспомогательная переменная, цикл пока не будет введено подходящее слово
        is_valid_input = 0
        while is_valid_input == 0:
            word_input = input().lower()
            if word_input.isalpha() and len(word_input) == 5 and word_input in words_list:
                input_list[i] = word_exam(word_input, correct_word)
                is_valid_input = 1
            else:
                print(f'{red}Неизвестное слово! {blue}Попробуйте еще раз:{white}')

        # Проверка на соответствие слова с загаданным
        if word_input == correct_word:
            print(f' {white}Wordle')
            print(*input_list, sep='\n')
            print(f'''{green}Вы победили!{white}
Хотите сыграть еще раз? {green}Y{white}/{red}N{white}: ''')
            if input().upper() == 'Y':
                return True
            return False

    # Если цикл не вернул ничего, значит игрок не отгадал слово и тем самым проиграл
    else:
        print(f' {white}Wordle')
        print(*input_list, sep='\n')
        print(f'''{red}Вы проиграли!
{blue}Загаданное слово: {green}{correct_word}{white}
Хотите сыграть еще раз? {green}Y{white}/{red}N{white}: ''')
        if input().upper() == 'Y':
            return True
        return False

# Цикл для повторения игр и для ее запуска
while True:
    if not wordle_game():
        break