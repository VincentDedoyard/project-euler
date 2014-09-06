import math

__author__ = 'Vincent Dedoyard'


class Primes():
    def __init__(self):
        self.primes = [2, 3]

    def _next_prime(self):
        """
        Gets the next prime and inserts into an internal list
        """

        potential_prime = self.primes[-1] + 2

        while not self.is_prime(potential_prime):
            potential_prime += 2

        self.primes.append(potential_prime)
        return potential_prime

    def is_prime(self, potential_prime):
        """
        Check whether a number is a prime
        """

        if potential_prime < 2:
            return False

        if potential_prime in self.primes:
            return True

        check_limit = int(math.sqrt(potential_prime)) + 1

        while check_limit > self.primes[-1]:
            self._next_prime()

        for prime in self.primes:
            if potential_prime % prime == 0:
                return False

            if prime > check_limit:
                return True

        return True

    def get_nth_prime(self, n):
        """
        Return the nth prime, where the first prime is 2
        """

        while len(self.primes) < n:
            self._next_prime()

        return self.primes[n - 1]

    def prime_after(self, number):
        """
        Get the first prime greater than a given number
        If the given number is prime, return the next prime
        """

        while number >= self.primes[-1]:
            self._next_prime()

        if self.is_prime(number):
            self._next_prime()
            i = self.primes.index(number)
            return self.primes[i+1]

        for prime in self.primes:
            if number < prime:
                return prime
