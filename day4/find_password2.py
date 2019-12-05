def get_digits(n):
    r = [n % 10, n//10 % 10, n//100 % 10, n//1000 % 10, n//10000 % 10, n//100000 % 10]
    return r

def increasing_digits(digits):
    result = True
    N = len(digits)
    for i in range(len(digits) - 1):
        result = result and digits[N-1 - i] <= digits[N-1 - i-1]

    return result

def two_adjacent_digits(digits):
    for i in range(len(digits) - 1):
        matching = digits[i] == digits[i+1]
        if matching:
            if i + 2 < len(digits):
                matching = matching and digits[i] != digits[i+2]
            if i - 1 >= 0:
                matching = matching and digits[i] != digits[i-1]
        if matching:
            return True

    return False


def run():
    puzzle_input = (387638, 919123)

    n_matching = 0
    for i in range(puzzle_input[0], puzzle_input[1]):
        digits = get_digits(i)
        r_increasing = increasing_digits(digits)
        r_adjacent = two_adjacent_digits(digits)
        if r_increasing and r_adjacent:
            n_matching += 1

    print("{} numbers match all criteria".format(n_matching))


if __name__ == '__main__':
    run()
