"""
2. Haz el ejercicio anterior usando una lista interna y eliminando elementos con el algoritmo de la criba de Eratóstenes.
Autor: Angel Fernández Ariza
Fecha: 2022-2023
"""
from collections.abc import Iterator


class PrimeIterator(Iterator):
    def __init__(self, max_value):
        self.__primes = self.__sieve_of_eratosthenes(max_value)
        self.current_value = 0

    @staticmethod
    def __sieve_of_eratosthenes(n):
        primes_candidates = list(range(2, n + 1))
        current_num = 0
        while primes_candidates[current_num] ** 2 < n:
            for j in primes_candidates:
                if j > primes_candidates[current_num] and j % primes_candidates[current_num] == 0:
                    primes_candidates.remove(j)
            current_num += 1
            # num_primes = list
            # num_primes = list(filter(lambda x: x % current_num != 0, primes_candidates))
        return primes_candidates

    def __next__(self):
        if self.current_value < len(self.__primes):
            prime = self.__primes[self.current_value]
            self.current_value += 1
            return prime
        else:
            raise StopIteration


if __name__ == '__main__':
    primes = list(PrimeIterator(30))
    print(primes)