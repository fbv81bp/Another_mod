'''setup'''
prime = 1949
pow_2 = 2048
test  = 1000000

'''the algorithm'''
def zalgorithm(up_for_mod, prime, pow_2, rec_depth):
    # doing magic
    divide   = up_for_mod // pow_2
    modulate = up_for_mod %  pow_2
    error    = pow_2      -  prime
    outcome  = modulate + error * divide
    # print(divide, modulate, error, outcome)
    # recursion
    if divide == 0:
        if outcome > prime:
            return outcome - prime, rec_depth 
        else:
            return outcome, rec_depth
    if outcome > prime and rec_depth < 15:
        outcome, rec_depth = zalgorithm(outcome, prime, pow_2, rec_depth + 1)
    # result
    return outcome, rec_depth 

'''thourough testing'''
print(zalgorithm(test, prime, pow_2, 0), test % prime)

'''even more testing'''
primes_n_pows = [[4051, 2**12], [3931, 2**12], [7877, 2**13], [232907, 2**18]]
tests  = [1765400057, 5078563000, 3012000123] 

for [prime, pow_2] in primes_n_pows:
    for test in tests:
        outcome, recursion_depth = zalgorithm(test, prime, pow_2, 0)
        print(outcome == test % prime, recursion_depth)

