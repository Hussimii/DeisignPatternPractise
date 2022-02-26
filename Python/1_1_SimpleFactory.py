"""
Create a Shape interface, entity classes implementing the Shape interface.
Define factory class ShapeFactory.
A FactoryPatternDemo, using the ShapeFactory to obtain Shape object.
    And it passes msg(CIRCLE/RECTANGLE/SQUARE) to ShapeFactory, to obtain the obejct.
"""


import abc


# common interface
class AbstractShape(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def draw(self):
        pass


# entity classes implementing the abstract interface.
class RectangleImplementsShape(AbstractShape):
    def __init__(self):
        print("this realize Interface")

    def draw(self):
        print("Inside Rectangle::draw() method.")


class CircleImplementsShape(AbstractShape):
    def __init__(sell):
        print("this realize Interface")

    def draw(self):
        print("Inside Circle::draw() method")


class SquareImplementsShape(AbstractShape):
    def __init__(self):
        print("this realize interface")

    def draw(self):
        print("Inside Square::draw() method")


class testAddNewShape(AbstractShape):
    def __init__(self):
        print("this realize interface")

    def draw(self):
        print("Inside test::draw() method")


# access to the abstract class Shape Interface.
class ShapeFactory(object):
    def __init__(self):
        print("ShapeFactory init.")

    def getShape(self, method):
        if method.lower() == 'rectangle':
            return RectangleImplementsShape()
        if method.lower() == 'square':
            return SquareImplementsShape()
        if method.lower() == 'circle':
            return CircleImplementsShape()
        if method.lower() == 'test':
            return testAddNewShape()


if __name__ == '__main__':
    shapeFactory = ShapeFactory()

    shap1 = shapeFactory.getShape('Rectangle')
    shap2 = shapeFactory.getShape('Square')
    shap3 = shapeFactory.getShape('Circle')
    test = shapeFactory.getShape('Test')

    shap1.draw()
    test.draw()
# shap2.draw()
# shap3.draw()
