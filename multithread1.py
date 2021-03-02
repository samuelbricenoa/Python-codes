import threading
import time
import sympy as s

startingtime = time.perf_counter()

threads = []
primes1 = []
primes2 = []
primes3 = []
primes4 = []
primes5 = []
primes6 = []
primes7 = []
primes8 = []
print(s.isprime(7))



def sieving(num):
    if num == 0:
        for numbers0 in range(2,12500000):
            if s.isprime(numbers0):
                primes1.append(numbers0)
    elif num == 1:
        for numbers1 in range(12500000,25000000):
            if s.isprime(numbers1):
                primes2.append(numbers1)
    elif num == 2:
        for numbers2 in range(25000000,37500000):
            if s.isprime(numbers2):
                primes3.append(numbers2)
    elif num == 3:
       for numbers3 in range(37500000,50000000):
            if s.isprime(numbers3):
                print(numbers3)
                primes4.append(numbers3)
    elif num == 4:
        for numbers4 in range(50000000,62500000):
            if s.isprime(numbers4):
                primes5.append(numbers4)
    elif num == 5:
        for numbers5 in range(62500000,75000000):
            if s.isprime(numbers5):
                primes6.append(numbers5)
    elif num == 6:
        for numbers6 in range(75000000,87500000):
            if s.isprime(numbers6):
                primes7.append(numbers6)
    elif num == 7:
        for numbers7 in range(87500000,100000000):
            if s.isprime(numbers7):
                primes8.append(numbers7)
    return










for num in range(8):
    t = threading.Thread(target=sieving, args = [num])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()

print (f'Finiished in {finish - startingtime} seconds')