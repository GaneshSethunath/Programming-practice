import math


def twenty_questions(low, high, num):
    tries = 0
    while True:
        if low > high:
            return -1
        else:
            mid = (low+high)//2
            tries += 1
            if mid == num:
                return tries
            elif mid > num:
                high = mid-1
            else:
                low = mid+1


if __name__ == "__main__":
    num = int(input(":"))
    print(f"{twenty_questions(0,math.pow(2,20), num)} tries taken to guess {num}. ")
