def step2_umbrella():
    print(
        'Какое небо голубое '
        'И светлый чистый горизонт '
        'Все потому что я сегодня '
        'Взял зонт '
    )


def step2_no_umbrella():
    print(
        'Зря, зря - the duck said'
    )


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
