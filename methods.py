import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, x0):
    result = 0
    for i in range(len(x)):
        p = 1
        for j in range(len(x)):
            if i != j:
                p *= (x0 - x[j]) / (x[i] - x[j])
        result += y[i] * p
    return result

def plot_lagrange(x, y, frequency):
    x_for_langrange = x[::frequency]
    y_for_langrange = y[::frequency]
    #dla analizy dodatkowej
    #x0 = x[::5]
    #x0 = x[::25]
    #in x0 jezeli chcemy zobaczyc jak dziala interpolacja dla analizy dodatkowej
    F = [lagrange_interpolation(x_for_langrange, y_for_langrange, x1) for x1 in x]
    plt.figure()
    plt.semilogy(x, y, 'red', label='full data')
    plt.semilogy(x, F, 'green', label='interpolated')
    plt.semilogy(x_for_langrange, y_for_langrange, 'bo', label='knots')
    plt.title('Lagrange interpolation' + ' (knot = ' + str(len(x_for_langrange)) + ')')
    plt.xlabel('Distance')
    plt.ylabel('Height')
    plt.legend()
    plt.show()
    
def cubic_spline_interpolation(x, y, x0):
    def F(x, y, x0):
        n = len(x)
        a = y
        h = [x[i] - x[i - 1] for i in range(1, n)]
        A = [[0] * n for _ in range(n)]
        for i in range(1, n - 1):
            A[i][i - 1] = h[i - 1]
            A[i][i] = 2 * (h[i - 1] + h[i])
            A[i][i + 1] = h[i]
        A[0][0] = 1
        A[n - 1][n - 1] = 1
        b = [0] + [3 * (a[i + 1] - a[i]) / h[i] - 3 * (a[i] - a[i - 1]) / h[i - 1] for i in range(1, n - 1)] + [0]
        c = [0] + [0] * (n - 1)
        for i in range(1, n):
            z = (A[i][i - 1] / A[i - 1][i - 1])
            A[i][i] = A[i][i] - z * A[i - 1][i]
            b[i] = b[i] - z * b[i - 1]
        c[n - 1] = b[n - 1] / A[n - 1][n - 1]
        for i in range(n - 2, -1, -1):
            c[i] = (b[i] - A[i][i + 1] * c[i + 1]) / A[i][i]
        b = [(a[i + 1] - a[i]) / h[i] - h[i] * (c[i + 1] + 2 * c[i]) / 3 for i in range(n - 1)]
        d = [(c[i + 1] - c[i]) / (3 * h[i]) for i in range(n - 1)]
        def S(x, a, b, c, d, x0):
            for i in range(n - 1):
                if x[i] <= x0 <= x[i + 1]:
                    return a[i] + b[i] * (x0 - x[i]) + c[i] * (x0 - x[i]) ** 2 + d[i] * (x0 - x[i]) ** 3
        return S(x, a, b, c, d, x0)
    return F(x, y, x0)

def plot_cubic(x, y, frequency):
    x_for_cubic = x[::frequency]
    y_for_cubic = y[::frequency]
    #dla analizy dodatkowej
    #x0 = x[::5]
    #x0 = x[::25]
    #in x0 jezeli chcemy zobaczyc jak dziala interpolacja dla analizy dodatkowej
    F = [cubic_spline_interpolation(x_for_cubic, y_for_cubic, x1) for x1 in x]
    plt.figure()
    plt.semilogy(x, y, 'red', label='full data')
    plt.semilogy(x, F, 'green', label='interpolated')
    plt.semilogy(x_for_cubic, y_for_cubic, 'bo', label='knots')
    plt.legend()
    plt.title('Cubic spline interpolation' + ' (knot = ' + str(len(x_for_cubic)) + ')')
    plt.xlabel('Distance')
    plt.ylabel('Height')
    plt.show()

