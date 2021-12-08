from functools import wraps

def decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)

    return wrapper



@decorator
def test_1(arq1, arq2):
    """
    Общее описание

    Примеры кода


    :param arq1: Описание параметра
    :param arq2:
    :return: Что возвращает (что происходит)

    Документация - это всегда первая строка с тройными кавычками
    """
    ...

@decorator
def test_2(arq1, arq2):
    """краткое описание"""
    ...

print(f" я вызываюсь {__name__}")
if __name__ == '__main__':
    print(test_1.__name__)
    print(test_1.__doc__)

    print(help(test_1))