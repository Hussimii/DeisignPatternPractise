# /usr/bin/python3
# coding = 'utf-8'
# filename: unit_mydict.py


class MyDict(dict):
    def __init__(self, **kwargs):
        super(MyDict, self).__init__(**kwargs)

    def __getattribute__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':
    d = MyDict(a=1, b=2)
    print(d['c'])
