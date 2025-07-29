# Big O -> O(n)
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


# Big O -> O(n)
def power(num, exp):
    if num == 0:
        return 0
    elif exp == 0:
        return 1
    elif exp == 1 or num == 1:
        return num
    elif exp > 1:
        return num * power(num, exp - 1)
    else:
        # return 1 / num * power(num, exp + 1)
        return power(num, exp + 1)/num


if __name__ == "__main__":
    print(f"Factorial of {5}: {factorial(5)}")
    print(f"5 to the power of 5 : {power(5, 5)}")
    print(f"0 to the power of -2 : {power(0, -2)}")
    print(f"-5 to the power of 3 : {power(-5, 3)}")
    print(f"5 to the power of -2 : {power(5, -2)}")
