from methods import *

def read_file(file):
    data = []
    with open(file, 'r') as f:
        for line in f:
            [x, y] = line.split(" ")
            data.append((float(x), float(y)))
    return data

def main():
    data = read_file('tczew_starogard.txt')
    x = [d[0] for d in data]
    y = [d[1] for d in data]
    frequency = 30
    plot_lagrange(x, y, frequency)
    plot_cubic(x, y, frequency)

if __name__ == '__main__':
    main()
    