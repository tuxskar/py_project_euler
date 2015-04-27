# Sum for all the even fibonacci number from 1 to 4 millions
import timeit

# times to execute for time comparative
times = 100000

# four millions
TARGET = 4*10**6


def by_my_self():
    prev, actual, next_v, ret_sum = 1, 2, 3, 2
    while next_v < TARGET:
        if next_v % 2 == 0:
            ret_sum += next_v
        prev, actual = actual, next_v
        next_v = prev + actual
    # print ret_sum
    return ret_sum


def using_some_hints():
    # we can see that the 3th value of the fibonacci numbers are always even, so we can check less and speed up
    prev, actual, next_v, ret_sum = 1, 1, 2, 0
    while next_v < TARGET:
        ret_sum += next_v
        prev = actual + next_v
        actual = prev + next_v
        next_v = prev + actual
    # print ret_sum
    return ret_sum


def ret_time(func):
    return timeit.timeit(func, number=times)


def print_ret(func):
    ret = ret_time(func)
    print 'Result: time {1} for {0} times'.format(times, ret)
    return ret


if __name__ == '__main__':
    print('By myself: ')
    r_my_self = print_ret(by_my_self)
    print('Using some hints: ')
    r_some_hint = print_ret(using_some_hints)
    fast_slower = [r_some_hint, r_my_self]
    if r_some_hint > r_my_self:
        fast_slower.reverse()
    print 'Best {} {} times faster'.format(fast_slower[0], fast_slower[1] / fast_slower[0] + 0.0)

# ##Result time comparative
# By myself:
# Result: time 0.569437026978 for 100000 times
# Using some hints:
# Result: time 0.212306976318 for 100000 times
# Best 0.212306976318 2.68213996945 times faster