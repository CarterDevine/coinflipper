import random
heads = 0
tails = 0

# computes 5000 coin tosses
for i in range(0, 5000):
    flip = random.randint(0, 1)
    if flip == 0:
        heads = heads + 1
    else:
        tails = tails + 1
print('total heads = ', heads, ' total tails = ', tails)
