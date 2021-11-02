# Advent of Code
# Day 4
# https://adventofcode.com/2019/day/4

input = "245318-765747"

min_value = 245318
max_value = 765747

# Puzzle 1
def check_password1(password):
    digits = str(password)

    has_double_digit = False
    for i in range(len(digits) - 1):
        if digits[i] > digits[i+1]:
            return False
        if digits[i] == digits[i+1]:
            has_double_digit = True

    if not has_double_digit:
        return False

    return True

count = 0
for password in range(min_value, max_value, 1):
    if check_password1(password):
        count += 1
print("First Puzzle:", count)


# Puzzle 2
def check_password2(password):
    digits = str(password)

    has_double_digit = False
    for i in range(len(digits) - 1):
        if digits[i] > digits[i+1]:
            return False
    for i in range(len(digits) - 3):
        if digits[i] == digits[i+1] and digits[i] != digits[i+2] and digits[i] != digits[i+3]:
            has_double_digit = True
    
    if not has_double_digit:
        return False

    return True

count = 0
for password in range(min_value, max_value, 1):
    if check_password2(password):
        print(password)
        count += 1
print("Second Puzzle:", count)
