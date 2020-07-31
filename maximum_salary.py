def maximum_salary(a):
    max_sal = []
    n = len(a)
    ones = [-1]
    tens = [-1]
    hundreds = [-1]
    for i in a:
        if i//10 == 0:
            ones.append(i)
        elif i//100 == 0:
            tens.append(i)
        else:
            hundreds.append(i)

    while n > 0:
        maxm = max(ones)
        pos = 1
        if maxm < max(tens)//10:
            maxm = max(tens)
            pos = 10
        if (maxm < max(hundreds)//10 and pos == 10) or (maxm < max(hundreds)//100 and pos == 1):
            maxm = max(hundreds)
            pos = 100
        max_sal.append(str(maxm))
        n -= 1
        if pos == 1:
            ones.remove(maxm)
        elif pos == 10:
            tens.remove(maxm)
        else:
            hundreds.remove(maxm)

    return "".join(max_sal)


if __name__ == "__main__":

    a = list(map(int, input().split()))
    print(maximum_salary(a))
