# Sieve of Eratosthenes
# Written in Python 3.10.3

""" 
In mathematics, the sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to any given limit.
It does so by iteratively marking as composite (i.e., not prime) the multiples of each prime,
starting with the first prime number, 2.
The multiples of a given prime are generated as a sequence of numbers starting from that prime,
with constant difference between them that is equal to that prime.
This is the sieve's key distinction from using trial division to sequentially test each candidate number for divisibility by each prime.
Once all the multiples of each discovered prime have been marked as composites,
the remaining unmarked numbers are primes.
"""


def sieve_of_eratosthenes(n):
    """prints prime numbers in given rnage n"""
    numbers = [True for i in range(n+1)]
    num = 2
    while num * num <= n:
        if numbers[num] is True:
            for i in range(num * num, n+1, num):
                numbers[i] = False
        num += 1

    # Print all prime numbers
    print(numbers)
    for num in range(2, n+1):  
        if numbers[num]:
            print(num)


# Driver code
if __name__ == '__main__':
    n = int(input("Enter a number : "))
    print(f"Following are the prime numbers smaller than or equal to {n}")
    sieve_of_eratosthenes(n)
