'''setup'''
prime = 1949
pow_2 = 2048
test  = 1000000

'''the algorithm'''
def zalgorithm(up_for_mod, prime, pow_2):
    # doing magic
    error = pow_2 -  prime
    while True:    
        divide   = up_for_mod // pow_2
        modulate = up_for_mod %  pow_2
        up_for_mod  = modulate + error * divide
        if divide == 0:
            break
    if up_for_mod > prime:
        up_for_mod -= prime
    return up_for_mod

'''thourough testing'''
print(zalgorithm(test, prime, pow_2), test % prime)

'''even more testing'''
primes_n_pows = [[4051, 2**12], [3931, 2**12], [7877, 2**13], [232907, 2**18]]
tests  = [1765400057, 5078563000, 3012000123] 

for [prime, pow_2] in primes_n_pows:
    for test in tests:
        outcome = zalgorithm(test, prime, pow_2)
        print(outcome == test % prime)

