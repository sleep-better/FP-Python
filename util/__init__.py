from functools import partial


def get_value(data, i):
    return data[i]


fst = partial(get_value, i=0)
snd = partial(get_value, i=1)


def find(func, lst):
    return next(filter(func, lst))
