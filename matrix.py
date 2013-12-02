from __future__ import division
import numpy


def T(a):
    t = numpy.eye(4, 4)
    t[0][2] = t[1][3] = a
    return t


def S(angle):
    return numpy.array([[numpy.cos(angle), numpy.sin(angle), 0, 0],
                            [-numpy.sin(angle), numpy.cos(angle), 0, 0],
                            [0, 0, numpy.cos(angle), numpy.sin(angle)],
                            [0, 0, -numpy.sin(angle), numpy.cos(angle)]])


def Zp():
    return numpy.array([[-1, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, -1, 0],
                        [0, 0, 0, 1]])


def Zr(r, angle):
    return numpy.array([[-1, 0, 0, 0],
                    [0, 1, 0, 0],
                    [2/(r * numpy.cos(angle)), 0, -1, 0],
                    [0, (-2 * numpy.cos(angle))/r, 0, 1]])

