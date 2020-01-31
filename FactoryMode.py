# coding = utf-8

"""
Without a union factory class to create all objects.
Provide diff factories for diff products.
-> every product have a relavent factory.
"""

# Define an interface to build object. leave subclasses decide which class to instantiate.

import abc


# 1. abstract interface for cars.
class AbstractCar(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __repr__(self):
        pass


# 2. entity car classes.

class Mercedes(AbstractCar):
    def __init__(self):
        print("access car interface")

    def __repr__(self):
        return "Mercedes-Benz"


class BMW(AbstractCar):
    def __init__(self):
        print("access car interface")

    def __repr__(self):
        return "BMW"


# 3. AbstractFactory

class AbstractFactory(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def produceCar(self):
        pass


# 4. subclass Car Factory

class MercedesFactory(AbstractFactory):
    def __init__(self):
        print("Factory interface accessed.")

    def produceCar(self):
        return Mercedes()


class BMWFactory(AbstractFactory):
    def __init__(self):
        print("Factory interface accessed.")

    def produceCar(self):
        return BMW()


if __name__ == '__main__':
    car1 = MercedesFactory().produceCar()
    car2 = BMWFactory().produceCar()
    print(car1, car2)
