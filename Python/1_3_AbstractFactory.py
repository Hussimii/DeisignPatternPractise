# coding = utf-8

# Define an interface to build object. leave subclasses decide which class to instantiate.

import abc


# 1. abstract interface for cars.
class AbstractCar(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __repr__(self):
        pass


# 2. entity car classes.

class Mercedes_C63(AbstractCar):
    def __init__(self):
        # print("access car interface")
        pass

    def __repr__(self):
        return "Mercedes-Benz: C63"


class BMW_M3(AbstractCar):
    def __init__(self):
        # print("access car interface")
        pass

    def __repr__(self):
        return "BMW: M3"


class Audi(AbstractCar):
    def __init__(self):
        # print("access car interface")
        pass

    def __repr__(self):
        return "Audo A6L"


# suv
class Mercedes_G63(AbstractCar):
    def __init__(self):
        # print("access car interface")
        pass

    def __repr__(self):
        return "Mercedes-Benz: G63"


class BMW_X5(AbstractCar):
    def __init__(self):
        # print("access car interface")
        pass

    def __repr__(self):
        return "BMW: X5"


# 3. AbstractFactory

class AbstractFactory(object):

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def produceCar(self):
        pass

    @abc.abstractmethod
    def produceSUV(self):
        pass


# 4. subclass Car Factory

class MercedesFactory(AbstractFactory):
    def __init__(self):
        print("Factory interface accessed.")

    def produceCar(self):
        return Mercedes_C63()

    def produceSUV(self):
        return Mercedes_G63()


class BMWFactory(AbstractFactory):
    def __init__(self):
        print("Factory interface accessed.")

    def produceCar(self):
        return BMW_M3()

    def produceSUV(self):
        return BMW_X5()


class AudiFactory(AbstractFactory):
    def __init__(self):
        print("Factory interface accessed.")

    def produceCar(self):
        return Audi()


if __name__ == '__main__':
    car1 = MercedesFactory().produceCar()
    car2 = BMWFactory().produceCar()
    car3 = AudiFactory().produceCar()
    print(car1, car2, car3)

    suv1 = MercedesFactory().produceSUV()
    suv2 = BMWFactory().produceSUV()
    print(suv1, suv2)
