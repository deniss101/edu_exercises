from random import choice, sample

ru_alphabet = 'АаБбВвГгДдЕеЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя'
word_list = ['безопасность', 'инструмент', 'успех', 'платье', 'стоимость',
'костюм', 'взаимодействие', 'мгновение', 'блок', 'система', 'звук', 'сомнение',
'ящик', 'частность', 'переговоры', 'лидер', 'палата', 'основание', 'институт',
'брат', 'газета', 'писатель', 'роман', 'существо', 'запас', 'редактор']


def get_word():
    '''
    Загадывает случайное слово из списка слов word_list

    '''
    return choice(word_list).upper()


def display_hangman(tries):
    '''
    Возвращает визуализацию оставшихся попыток.

    '''
    stages = ['X', 'o', 'oo', 'ooo', 'oooo', 'ooooo', 'oooooo', 'ooooooo']
    return stages[tries]


def fail_answer(tries, guessed_letters, word_completion):
    '''
    Отображает оставшиеся поппытки, названные буквы и сколько позиций в слове отгадано.

    '''
    print(f'Попытки |{display_hangman(tries)}|')
    print('Названные буквы: ', *guessed_letters)
    print('Слово: ', word_completion)


def new_game():
    '''
    Предлагает повторить игру

    '''
    new_game = input('Сыграем ещё? д / н ')
    if new_game == 'д':
        play(get_word())


def play(word):
    '''
    Проверяет входит ли загаданная буква в слово.
    Контроль оставшихся попыток и состояния выигрыша/проигрыша.

    '''
    word_completion = '_' * len(word)
    guessed_letters = []
    tries = 7
    hint = 0
    print('Сыграем!')
    print(f'Попытки |{display_hangman(tries)}|')
    print('Слово: ', word_completion)

    while tries > 0:
        new_letter = input('Введите букву: ').upper()
        print()

        while not new_letter.isalpha() or not new_letter in ru_alphabet:
            print('Введён некорректный символ')
            new_letter = input('Введите слово или букву: ').upper()

        for c in new_letter:
            if c in guessed_letters:
                print('Такая буква уже была')
                fail_answer(tries, guessed_letters, word_completion)
                break
            else:
                guessed_letters.append(c)

            if c in word:
                print('Вы угадали букву')
                hint -= 1
                for i in range(len(word)):
                    if word[i] == c:
                        word_completion = word_completion[:i] + c + word_completion[i + 1:]
                fail_answer(tries, guessed_letters, word_completion)

            if c not in word:
                print('Такой буквы нет в этом слове')
                tries -= 1
                hint += 1
                fail_answer(tries, guessed_letters, word_completion)

            if word_completion == word:
                print('Поздравляем, вы угадали слово! Вы победили!')
                new_game()
                return

        if hint == 3:
            print()
            need_hint = input('| Нужна подсказка? д / н |')
            if need_hint == 'д':
                print('Слово содержит: ', *sample(word, 3))

    if tries == 0:
        print('\n', 'GAME OVER')
        print('Загаданное слово: ', word.capitalize())
        new_game()
        return


play(get_word())
