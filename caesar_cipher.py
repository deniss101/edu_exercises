def get_param() -> tuple:
    '''
    Определения параметров работы. 
    Выбор языка, действия (кодирование/декодирование фрызы, подбор ключа для расшифровки).
    Ввод фразы для обработки.

    '''
    lang = input('Русский или английский: РУ / АН ').lower()
    shift = int(input('Шаг сдвига: >0 - шифруем, <0 - дешифруем, =0 - перебор ключей '))
    phrase = input('Введите фразу: ')
    return lang, shift, phrase


def cipher(lang: str, shift: int, phrase: int):
    '''
    Шифрование/дешифрование входной фразы с учётом указанных параметров
    Вывод зашифрованной фразы.

    '''
    if lang == 'ру':
        letters = 32
        for c in phrase:
            if c in ',.?! ':
                print(c, end='')
            elif 1040 <= ord(c) <= 1071:
                print(chr((ord(c) + shift - 1040) % letters + 1040), end='')
            elif 1072 <= ord(c) <= 1103:
                print(chr((ord(c) + shift - 1072) % letters + 1072), end='')
    if lang == 'ан':
        letters = 26
        for c in phrase:
            if c in ',.?! ':
                print(c, end='')
            elif 65 <= ord(c) <= 90:
                print(chr((ord(c) + shift - 65) % letters + 65), end='')
            elif 97 <= ord(c) <= 122:
                print(chr((ord(c) + shift - 97) % letters + 97), end='')


def new_cipher():
    '''
    Выбор действия при подборе ключа для дешифровки.

    '''
    lang, shift, phrase = get_param()
    if shift == 0:
        if input('Шифрование или дешифрование: Ш / Д ').lower() == 'д':
            shift = -shift
            if lang == 'ру':
                for i in range(1, 31):
                    print(i, end=' ')
                    print(cipher(lang, i, phrase))
            if lang == 'ан':
                for i in range(1, 25):
                    print(i, end=' ')
                    print(cipher(lang, i, phrase))
    else:
        cipher(lang, shift, phrase)

    print()
    again = input('Работаем ещё? да / нет ')
    if again in ['да', 'д', 'y']:
        new_cipher()


new_cipher()
