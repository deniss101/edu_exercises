import random


print('Добро пожаловать в числовую угадайку', '\n')


def is_valid(number, n):
    '''
    Проверка введённого числа, требуется целое от 1 до введенной границы.

    '''
    return number.isdigit() and 1 <= int(number) <= int(n)


def rand_n():
    '''
    Получение и проверка границы и генерация числа для угадывания.
    
    '''
    n = input(f'\nУгадаем число?' '\n' 'Введите верхнюю границу: ')
    while not n.isdigit():
        print('Ожидаю целое число', '\n')
        n = input('Введите верхнюю границу: ')
    return n, random.randint(1, int(n))


n, rand = rand_n()
tries = 0
while True:
    number = input(f'\nВведите число от 1 до {n}: ')
    if is_valid(number, n):
        valid_number = int(number)
        if valid_number < rand:
            tries += 1
            print('Число меньше загаданного, попробуйте еще')
        elif valid_number > rand:
            tries += 1
            print('Число больше загаданного, попробуйте еще')
        elif valid_number == rand:
            print('\n', '   |   Победа!   |', sep='')
            print(f'Угадано за {tries} попыток')
            new_game = input('Сыграем ещё? да / нет ')
            if new_game == 'да':
                n, rand = rand_n()
                continue
            else:
                print('Спасибо, что играли, bye', '\n')
                break
