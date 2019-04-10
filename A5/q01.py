"""COMP1510 Assignment 5: Back to basics"""

# Trae Bold
# A01072453
# JAN 11, 2019


def sum_of_primes(upper_bound: int) -> int:
    if upper_bound < 0:
        raise ValueError("Only positive integers accepted as upper bounds!")
    else:
        prime_list = []
        for num in range(2, upper_bound + 1):
            # Prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    prime_list.append(num)
        return sum(prime_list)


def main():
    try:
        print(sum_of_primes(-1))
    except ValueError as e:
        print(e)


if __name__=='__main__':
    main()
