import random

# max er antall kuler bollen
# draws er antallet kuler vi trekker

def lottery(max, draws):

    # tilgjengelige tall
    numbers = []

    for i in range(max):
        numbers.append(i+1)

    #print(numbers)

    lottery_numbers = []

    for j in range(draws):
        x = random.choice(numbers)
        numbers.remove(x)
        lottery_numbers.append(x)

    #print(numbers)
    lottery_numbers.sort()
    print(lottery_numbers)
    

lottery(30,7)