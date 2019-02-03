def compound_interest(P, r, n, t):
    """Calculate earned compound interest.

    A function that calculates the balance using compound interest formula.
    PARAM: P: amount originally deposited into the account.
        r: annual interest rate.
        n: number of times per year interest compounded.
        t: number of years the account will be left alone to grow.
    PRECONDITION: P must be a float.
        r must be a float.
        n must be an int.
        t is an int.
    RETURN: the correct amount money in the account after ekapsed time as a float.
    """
    A = float(P) * (1 + (float(r) / int(n))) ** int(n * t)
    return A



def main():
    print(compound_interest(1,1,1,1))

if __name__ == "__main__":
    main()