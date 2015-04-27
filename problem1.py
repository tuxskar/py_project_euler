import timeit

times = 100000

# using SumDivisibleBy
TARGET = 1000


def sum_divisible_by(n):
    # 3+6+9+12+...+999=3*(1+2+3...+333)
    # 5+10+15+...+995=5*(1+2+3...+199)
    # 333=999/3 and 199=999/5
    # and finally 1+2+3+4+...+p = p*(p+1)/2
    p = (TARGET - 1) / n
    return n * (p * (p + 1)) / 2


def by_my_self():
    return sum([x for x in range(1000) if not x % 3 or not x % 5])


def using_sum_divide_by():
    return sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15)


def ret_time(func):
    return timeit.timeit(func, number=times)


def print_ret(func):
    ret = ret_time(func)
    print 'Result: time {1} for {0} times'.format(times, ret)
    return ret


print 'Using sumDivisibleBy sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15)'
r_sum_div = print_ret(using_sum_divide_by)
print('By myself sum([x for x in range(1000) if not x % 3 or not x % 5])')
r_my_self = print_ret(by_my_self)
fast_slower = [r_sum_div, r_my_self]
if r_sum_div > r_my_self:
    fast_slower.reverse()
print 'Best {} {} times faster'.format(fast_slower[0], fast_slower[1] / fast_slower[0] + 0.0)

## Result
# Using sumDivisibleBy sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15)
# Result: time 0.0946531295776 for 100000 times
# By myself sum([x for x in range(1000) if not x % 3 or not x % 5])
# Result: time 15.113296032 for 100000 times
# Best 0.0946531295776 159.67032574 times faster
