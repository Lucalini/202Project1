# int -> booelan
# Given integer n, returns True or False based on reachabilty of goal
def bears(n):
    if n == 42:
        return True
    if n < 42 :
        return False

    if n % 2 == 0:
        if bears(n - n // 2):
            return True

    digit1 = int(str(n)[0])
    digit2 = int(str(n)[1])

    if (n % 3 == 0 or n % 4 == 0) and (digit1 != 0 and  digit2  != 0) :
        if (bears(n-(int(digit1)*int(digit2)))):
            return True


    if n % 5 == 0:
        if bears(n - 42):
            return True

    return False

print(bears(5852))

