def fabric_decorators(arq_decoration):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)
        return wrapper
    return fabric_decorators


 def decorator(fn):
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)
        return wrapper
    return fabric_decorators

@decorator
def test_1(arq):
    return arq


@fabric_decorators(123)
def test_1(arq):
    return arq

if __name__ == '__main__':
    test_1(5)
