# Выполнение и проверка первого задания ###############################################################################

def first_task(inpt: str) -> str:
    """
    Основой решения задачи являются генераторы - с их помощью мы отбираем нужные элементы из input (неравные нулю)
    в новую переменную output. После отбора нужных элементов мы вычитаем длину output из длины input, чтобы понять,
    сколько в output нужно добавить нулей. Добавляем к output недостаюшие нули и возвращаем результат.
    :param inpt: список/строка/число int
    :return: строка с числами, отсортированная по принципу "нули в конец"
    """
    inpt = inpt.split()  # получаем список, избавляемся от пробелов
    output = [elem for elem in inpt if elem != '0']  # создаем список, собираем все, что не равно нулю
    output.append('0 ' * (len(inpt) - len(output)))  # прибавляем к созданному списку столько нулей, сколько нужно
    return ''.join(elem + ' ' for elem in output)  # возвращаем строку в фомате, указанном в условии задачи


print(' Первое задание')
inpt = input('Введите список/строку/число int ')
print(first_task(inpt))

# Выполнение и проверка второго задания ################################################################################

from re import findall


def second_task(inpt: str) -> str:
    """
    Простое решение с помощью генераторов - составляем списки гласных и согласных и высчитываем их длину
    :param inpt: любая строка
    :return: количество гласных и согласных
    """
    vowels = 'aeiouyауоыэяюёие'
    vowels = len([elem for elem in inpt.lower() if elem in vowels])
    consonants = 'bcdfghjklmnpqrstvwxzбвгджзйклмнпрстфхцчшщ'
    consonants = len([elem for elem in inpt.lower() if elem in consonants])
    return f'Гласных: {vowels}, согласных: {consonants}'


def second_task_re(inpt: str) -> str:
    """
    Еще более простое решение с помощью регулярных выражений - получаем список всех совпадений с шаблоном и
    вычисляем его длину
    :param inpt: любая строка
    :return: количество гласных и согласных
    """
    vowels = 'aeiouyауоыэяюёие'
    vowels = len(findall(f'[{vowels}]', inpt.lower()))
    consonants = 'bcdfghjklmnpqrstvwxzбвгджзйклмнпрстфхцчшщ'
    consonants = len(findall(f'[{consonants}]', inpt.lower()))
    return f'Гласных: {vowels}, согласных: {consonants}'


print('\n Второе задание')
inpt = input('Введите строку ')
print(second_task_re(inpt))

# Выполнение и проверка третьего задания ###############################################################################


def third_task(frm: list, whr: list) -> str:
    """
    Простое условие для хода по вертикали/горизонтали - координаты x либо y обоих положений равны.
    Более сложное условия для хода по диагонали - модули разностей x и y координат должны быть равны.
    :param frm: x, y координаты положения ферзя в виде списка [x, y]
    :param whr: x, y координаты, проверки в виде списка [x, y]
    :return: Да или Нет, в зависимости от того, может ли ферзь передвинуться на указанные координаты
    """
    frm = [int(elem) for elem in frm]
    whr = [int(elem) for elem in whr]
    if frm[0] == whr[0] or frm[1] == whr[1] or abs(frm[0] - whr[0]) == abs(frm[1] - whr[1]):
        return 'Да'
    else:
        return 'Нет'


print('\n Третье задание')
frm = [input('Введите x-координату ферзя '), input('Введите y-координату ферзя ')]
whr = [input('Введите x-координату куда идти '), input('Введите y-координату куда идти ')]
print(third_task(frm, whr))
