from random import choice


answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да',
'Можешь быть уверен в этом', 'Мне кажется да', 'Вероятнее всего',
'Хорошие перспективы', 'Знаки говорят - да', 'Да',
'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать',
'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять',
'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет',
'Перспективы не очень хорошие', 'Весьма сомнительно']

name = input('Как тебя зовут? ')
print(f'Привет {name}, я магический шар, и я знаю ответ на любой твой вопрос.\n')

while True:
    question = input(f'Задай же свой вопрос, {name}: \n')
    print(f'Мой ответ: {choice(answers)}\n')
    new_question = input('У тебя остались вопросы ко мне? да/нет ')
    if new_question == 'нет':
        print('Возвращайся если возникнут вопросы!')
        break
