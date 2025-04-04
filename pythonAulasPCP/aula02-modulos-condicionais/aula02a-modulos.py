import math
from math import sqrt

num = int(input('digite um num:'))
#raiz = math.sqrt(num)
raiz = sqrt(num)
print(f'a raiz de {num} é {raiz:.2f}')

graus = 45
radiano = graus / 180 * math.pi
seno = math.sin(radiano)
print(seno)

import random
num_random = random.random()
print(num_random)

num_int = random.randint(1,10)
print(num_int)

