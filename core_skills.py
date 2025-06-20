import random

rand_list = random.sample(range(20), 10)

list_comprehension_below_10 = [i for i in rand_list if i < 10]

filter_list_below_10 = list(filter(lambda i: i < 10, rand_list))
