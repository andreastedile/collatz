from collatz import collatz
from utils import timeit


@timeit
def compute(n_from, n_to):
    for n in range(n_from, n_to):
        print(collatz(n))


if __name__ == '__main__':
    while True:
        n_from = int(input('From: '))
        n_to = int(input('To: '))
        compute(n_from, n_to)
