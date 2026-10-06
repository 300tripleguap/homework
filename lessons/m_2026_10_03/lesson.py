# ТВОЙ КОД
from time import sleep

def long_condition_count(result=False):  # имитация долгой проверки условия
    sleep(3)
    return result

def ticket_price(age):
    """
    Как только один if или elif сработал, то остальные НЕ выполняются в данном блоке
    """
    if long_condition_count(result=True):
        print('1')
    elif long_condition_count():
        print('2')
    elif long_condition_count():
        print('3')
    else:
        print('3')
    return 'Конец'

print(ticket_price(-1))


def ticket_price(age):
    """
    Все if здесь отдельные НЕ зависимые друг от друга условия и они будут проверятся все.
    """
    if long_condition_count(result=True):
        print('1')

    if long_condition_count():
        print('2')
        
    if long_condition_count():
        print('3')

    return 'Конец'

print(ticket_price(-1))