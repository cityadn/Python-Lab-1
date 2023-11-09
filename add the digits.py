def sum_of_digits(number):
    sum = 0
    while number % 10 != 0:
        number = number * 10
    while number > 0:
        remainder = number%10
        sum = sum + remainder
        number = int(number/10)
    return int(sum)


number = 341.2
print(format(sum_of_digits(number)))


