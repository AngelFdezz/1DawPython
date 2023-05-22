"""
1. Crea el iterador PrimeIterator que permita iterar sobre la lista de números primos, desde 2 hasta uno dado como máximo.

Ejemplo: "primes = list(PrimeIterator(15)) devolverá [2, 3, 5, 7, 11, 13]
Autor: Angel Fernández Ariza
Fecha: 2022-2023
"""
import math


def _is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


class PrimeIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current_value = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current_value += 1
        while not _is_prime(self.current_value):
            self.current_value += 1
        if self.current_value > self.max_value:
            raise StopIteration
        return self.current_value

if __name__ == '__main__':
    primes = list(PrimeIterator(30))
    print(primes)