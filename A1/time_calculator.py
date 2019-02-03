def time_calculator(seconds):
    """Calculate seconds.

    A function that converts seconds to day, hours, minutes, and seconds.
    PARAM: int, seconds.
    PRE: number must be an integer.
    RETURN: returns number of days, hours, minutes and seconds as integer in a list.
    >>>time_calculator(61)
    [0, 0, 1, 1]
    >>>time_calculator(2019)
    [0, 0, 33, 19]
    >>>time_calculator(360709)
    [4, 4, 11, 49]
    """
    calculator = []
    calculator.append(seconds // 86400)
    hours = seconds % 86400
    calculator.append(hours // 3600)
    minutes = hours % 3600
    calculator.append(minutes // 60)
    seconds = minutes % 60
    calculator.append(seconds)

    return calculator
def main():
    print(time_calculator(360709))

if __name__ == "__main__":
    main()