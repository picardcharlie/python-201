# Adapt your Generator expression from the previous exercise:
# Don't print anything, and run a floor division by 1111 on it.
# What numbers do you get?

nums = range(1, 1000000)

gen_1111 = (x for x in nums if x%1111 == 0)

for x in gen_1111:
    print(x // 1111)

# Prints out all the numbers between 1-900