import random
import math

n = random.randint(1, 10000)
array = [random.randint(0, 100) for i in range(n)]

next_power_of_two = 2 ** int(math.ceil(math.log2(n)))
array.extend([0] * (next_power_of_two - n))

print("Массив:", array)