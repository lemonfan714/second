from random import randint

same_digits = set()
while same_digits == set():
    num_1 = set(str(randint(1, 100)))
    num_2 = set(str(randint(1, 100)))

    same_digits = num_1.intersection(num_2)

    if same_digits != set():
        print('ЧИСЛА СОВПАЛИ')
        print(same_digits)
        print(num_1, num_2)
    else:
        print('Not founded')
        print(num_1, num_2)