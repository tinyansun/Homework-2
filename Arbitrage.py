liquidity = {
    ("tokenA", "tokenB"): (17, 10), 
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

def my_swap(input_token, output_token, num):
    new_num = num * 99.7 / 100
    new_output_token = input_token * output_token / (input_token + new_num)
    tokens_earned = (output_token - new_output_token)
    new_balance_in = input_token + new_num
    new_balance_out =  new_output_token
    return tokens_earned


# initial
path = []
path.append("tokenB")

# B -> A
out_1st = my_swap(10, 17, 5)
path.append("tokenA")
print(out_1st)
# A -> C
out_2nd = my_swap(11, 7, out_1st)
path.append("tokenC")
print(out_2nd)
# C -> E
out_3rd = my_swap(10, 8, out_2nd)
path.append("tokenE")
print(out_3rd)

# E -> D
out_4th = my_swap(25, 60, out_3rd)
path.append("tokenD")
print(out_4th)
# D -> C
out_5th = my_swap(12, 30, out_4th)
path.append("tokenC")
print(out_5th)
# C -> B
out_6th = my_swap(4, 36, out_5th)
path.append("tokenB")
print(out_6th)

# print path
print("path: ", end = '')
for i in range(len(path)):
    if (i == len(path) - 1):
        print(path[i], end='')
        print(",", end='')
    else:
        print(path[i], end='')
        print("->", end='')
print("tokenB balance=", end='')
print(out_6th, end='')
print('\n')