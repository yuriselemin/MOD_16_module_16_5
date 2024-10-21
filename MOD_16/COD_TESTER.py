import random
import time



# print([x for x in range(1,11)])
#
#
#
# random_numbers = [random.randint(50, 1000) for _ in range(10)]
# print(random_numbers)

num  = [random.randint(10, 20) for _ in range(3)]
for n in num:
    # time.sleep(random.randint(1, 5))
    print(n)
    time.sleep(1)


