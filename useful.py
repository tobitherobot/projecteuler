def rwh_primes1(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    # returns a list of primes < n
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5) + 1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1) // (2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]

def is_prime(n):
    if n<3:
        if n==2:
            return True
        else:
            return False
    elif n%2==0:
        return False
    d = 3
    while d*d <= n:
        if n % d == 0:
            return False
        d += 2
    return True