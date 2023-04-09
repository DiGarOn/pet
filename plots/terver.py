# -*- coding=utf-8 -*-
import matplotlib.pyplot as plt
import numpy

def makeData ():
    # Строим сетку в интервале от -10 до 10, имеющую 100 отсчетов по обоим координатам
    x = numpy.linspace(0, 10, 100)
    y = numpy.linspace(0, 10, 100)
    z = numpy.linspace(0, numpy.pi, 100)
    # Создаем двумерную матрицу-сетку
    # xgrid, ygrid, zgrid = numpy.meshgrid(x, y, z)
    # В узлах рассчитываем значение функции
    for x_i in x:
        for y_i in y:
            for z_i in z:
                if not (x_i < 2*numpy.cos(z_i) and y_i < -2*numpy.sin(z_i)):
                    print(x_i, y_i)
    # z = numpy.sin (xgrid) * numpy.sin (ygrid) / (xgrid * ygrid)
    return x, y, z


if __name__ == '__main__':
    x, y, z = makeData()
    fig = plt.figure()
    axes = fig.add_subplot(projection='3d')
    # !!!
    axes.plot_surface(x, y, z)
    plt.show()