def get_digits(n):
    r = [n % 10, n//10 % 10, n//100 % 10, n//1000 % 10, n//10000 % 10, n//100000 % 10]
    return r

def increasing(digits):
    result = True
    N = len(digits)
    for i in range(len(digits) - 1):
        result = result and digits[N-1 - i] <= digits[N-1 - i-1]

    return result

def adjacent(digits):
    result = False
    for i in range(len(digits) - 1):
        result = result or digits[i] == digits[i+1]

    return result


def run():
    puzzle_input = (387638, 919123)

    n_matching = 0
    for i in range(puzzle_input[0], puzzle_input[1]):
        digits = get_digits(i)
        r_increasing = increasing(digits)
        r_adjacent = adjacent(digits)
        if r_increasing and r_adjacent:
            # print("{} matches both criteria".format(i))
            n_matching += 1

        # if i <= puzzle_input[0] + 3:
        #     print(i, digits)

    print("{} numbers match all criteria".format(n_matching))


if __name__ == '__main__':
    run()
