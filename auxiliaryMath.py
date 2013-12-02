# -*- coding: koi8_r -*-
from __future__ import division
#TODO:отделить линейную алгебру от работы с массивами
import numpy


class AuxiliaryMath:
    @staticmethod
    def angle(vector1, vector2):
        cosAngle = numpy.vdot(vector1, vector2) / (numpy.linalg.norm(vector1) * numpy.linalg.norm(vector2))
        return numpy.arccos(cosAngle)

    @staticmethod
    def reducedAngle(vector1, vector2):
        return numpy.pi - AuxiliaryMath.angle(vector1, vector2)

    @staticmethod
    def closedCalculate(func, array):
        results = []
        i = 0
        for item in array:
            result = func(item, array[i - 1])
            results.append(result)
            i += 1
        return results

    @staticmethod
    def rotateArray(array, direction='positive'):
        arrayCopy = array[:]
        if direction == 'positive':
            last = arrayCopy.pop(0)
            arrayCopy.append(last)
        else:
            first = arrayCopy.pop()
            arrayCopy.insert(0, first)
        return arrayCopy
        #rotates array at 1 position counterclockwise

    @staticmethod
    def adjustArrayIndex(index, arrayLength):
        if index < 0:
            return (arrayLength + index)
        elif index > arrayLength - 1:
            return (index - arrayLength)
        else:
            return index

    @staticmethod
    def normal(vector1, vector2):
        crossProduct = numpy.cross(vector1, vector2)
        norm = numpy.linalg.norm(crossProduct)
        return crossProduct / norm

    @staticmethod
    def pairs(array):
        return zip(array, AuxiliaryMath.rotateArray(array))

    @staticmethod
    def reverseCircleWalk(array, func, start=0):
        i = 0
        while i <= len(array):
            func(array[start - 1 - i])

    @staticmethod
    def matrixProduct(*factors):
        product = numpy.eye(factors[0].shape[0])
        for factor in factors:
            product = numpy.dot(product, factor)
        return product

    #TODO:исправить это безобразие
    @staticmethod
    def reversedMatrixProduct(*factors):
        product = numpy.eye(factors[0].shape[0])
        for factor in factors:
            product = numpy.dot(factor, product)
        return product

    #этот метод умеет перемножать матрицы в прямом порядке, причем делает это циклически(!indexOutOfRange)
    @staticmethod
    def matrixPiDirectOrder(factors, start, stop):
        print(factors[start:stop])
        return AuxiliaryMath.matrixProduct(*factors[start:stop])

    @staticmethod
    def matrixPiReversedOrder(factors, start, stop):
        return AuxiliaryMath.reversedMatrixProduct(*factors[start:stop])


    @staticmethod
    #TODO:заставить работать
    def matrixPiBackOrder(array, start, stop):
        return (AuxiliaryMath.matrixPiDirectOrder(reversed(array), start, stop))

    @staticmethod
    def arrayEqual(correctMatrix, ratedMatrix, precision=10e-16):
        return numpy.linalg.norm(correctMatrix - ratedMatrix) < precision

if __name__ == '__main__':
    a = numpy.array([0, 1])
    b = numpy.array([1, 1])
    vector1 = numpy.array([0, 1, 0])
    vector2 = numpy.array([1, 1, 0])
    print(AuxiliaryMath.angle(a, b))
    print(AuxiliaryMath.normal(vector1, vector2))
    print(AuxiliaryMath.closedCalculate(numpy.subtract, [a, b, a]))
    print(AuxiliaryMath.pairs([1, 2, 3]))
    piFactors = [numpy.array([[1, 2], [1, 1]]),
                 numpy.array([[0, 3], [4, 1]]),
                 numpy.array([[1, 7], [9, 0]]),
                 numpy.array([[1.2, 6], [0.9, 25]])]

    AuxiliaryMath.matrixPiDirectOrder(piFactors, 2, 1)
