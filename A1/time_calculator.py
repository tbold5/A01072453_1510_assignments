def time_calculator(seconds):
    """A time calculator

       A function that converts seconds to day, hours, minutes, and seconds
       PARAM: int, seconds
       PRE: number must be an integer
       RETURN: returns number of days, hours, minutes and seconds as integer in a list
    """
    minute = int(seconds) // 60
    hour = int(seconds) // 3600
    day = int(seconds) // 86400
    seconds = int(seconds)
    my_list = [day, hour, minute, seconds]

    return my_list

def main():
    print(time_calculator(60))

if __name__ == "__main__":
    main()