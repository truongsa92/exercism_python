def prime_factors(number):
    factors = []
    for factor in range(2, int(number**0.5)+1):
        while number % factor == 0:
            number /= factor
            factors.append(factor)
            if number == 1:
                break
    if number != 1:
        factors += [number]
    return factors

print(prime_factors(24))
print(prime_factors(13))