'''setup'''
prime = 1949     # a prime we want to find the modulus with
pow_2 = 2048     # the next power of 2 that is just larger than the prime
test  = 1000000  # the number whose modulus is being found

'''the algorithm'''
def zalgorithm(up_for_mod, prime, pow_2):
    error = pow_2 -  prime                     # at each division there is an error in the modulus caused by the difference between the power and the prime
    while True:    
        divide     = up_for_mod // pow_2       # characterizing the size of the error
        modulate   = up_for_mod %  pow_2       # approaches the designated outcome
        up_for_mod = modulate + error * divide # intermediate value between iterations: the total error's modulus will have to be found at the end
        if divide == 0:                        # when there isn't anything left to divide, the algorithm will nearly have finished
            break
    if up_for_mod > prime:                     # the last step is to check if the result has landed between the prime and the power
        up_for_mod -= prime                    # and correct that if necessary
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

