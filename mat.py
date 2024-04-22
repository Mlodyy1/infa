def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_digits_prime(n):
    return is_prime(sum(int(digit) for digit in str(n)))

def binary_sum_prime(n):
    return is_prime(sum(int(digit) for digit in bin(n)[2:]))

def super_b_prime(n):
    return is_prime(n) and sum_of_digits_prime(n) and binary_sum_prime(n)

def count_super_b_primes_in_range(start, end):
    count = 0
    super_b_primes = []
    for num in range(start, end + 1):
        if super_b_prime(num):
            count += 1
            super_b_primes.append(num)
    return count, super_b_primes

def save_super_b_primes_to_file(primes, filename):
    with open(filename, 'w') as file:
        for prime in primes:
            file.write(str(prime) + '\n')

# a)
ranges = [(2, 1000), (100, 10000), (1000, 100000)]
results_table = []
for i, (start, end) in enumerate(ranges, 1):
    count, super_b_primes = count_super_b_primes_in_range(start, end)
    results_table.append((i, f'<{start},{end}>', count))
    save_super_b_primes_to_file(super_b_primes, f'{i}.txt')

# b)
count_sum_of_digits_primes = sum(1 for num in range(100, 10000 + 1) if sum_of_digits_prime(num))
sum_of_super_b_primes = sum(num for num in range(100, 10000 + 1) if super_b_prime(num))

print("a) Wyniki:")
print("Nr przedziału | Przedział | Liczba wystąpień liczb „super B pierwszych”")
for row in results_table:
    print("{:<14} | {:<10} | {:<10}".format(*row))

print("\nb) Odpowiedzi:")
print("Ile jest liczb w przedziale <100,10000>, których suma cyfr jest liczbą pierwszą?")
print("Odp:", count_sum_of_digits_primes)
print("Czy suma wszystkich liczb „super B pierwszych” z przedziału <100,10000> jest liczbą pierwszą?")
print("Odp:", "Tak" if is_prime(sum_of_super_b_primes) else "Nie")
