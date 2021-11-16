import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt


def main(n, bound, func, poly_degree):
    '''
    :param n:
        Количество делений на промежутке
    :param bound:
        Левая и права граница
    :param func:
        Функция переменных
    :param poly_degree:
        Степень полинома при интерполяции
    '''


    left, right = bound

    if not n % 2:
        n -= 1

    x = np.linspace(left, right, n)

    cos_k = np.arange(0, n // 2 + 1, dtype=np.float64)
    sin_k = np.arange(1, n // 2 + 1, dtype=np.float64)

    V = np.zeros((n, n))

    V[:, ::2] = np.cos(cos_k * x[:, np.newaxis])
    V[:, 1::2] = np.sin(sin_k * x[:, np.newaxis])

    coeffs = la.solve(V, func(x))

    plot_x = np.linspace(left, right, 100)

    interpolant = 0 * plot_x

    for i, k in enumerate(cos_k):
        interpolant += coeffs[2 * i] * np.cos(k * plot_x)
    for i, n in enumerate(sin_k):
        interpolant += coeffs[2 * i + 1] * np.sin(n * plot_x)

    p = np.poly1d(np.polyfit(x, func(x), deg=poly_degree))

    plt.plot(plot_x, func(plot_x), "--", color="gray")
    plt.plot(x, func(x), "or")
    plt.plot(plot_x, interpolant)

    plt.plot(plot_x, p(plot_x), '-')

    plt.legend(['Функция', 'Точки', 'Фурье', 'Полиномы'], loc='best')
    plt.grid()
    plt.show()


if __name__ == '__main__':
    main(
        4,
        (-2, 2),
        lambda x: x ** 3,
        6
    )
