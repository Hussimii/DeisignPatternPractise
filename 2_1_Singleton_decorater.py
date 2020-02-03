from functools import wraps


def Singleton(cls):
    _singleton = {}
    @wraps(cls)
    def wrapSingleton(*args, **kwargs):
        if cls not in _singleton:
            _singleton[cls] = cls(*args, **kwargs)
        return cls(*args, **kwargs)
    return wrapSingleton


@Singleton
class A(object):
#    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)

print(a1, '\n', a2)
