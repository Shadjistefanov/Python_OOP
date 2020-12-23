def get_primes(num_list):
    prime_list = []
    for num in num_list:
        if num <= 1:
            continue
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num






print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))