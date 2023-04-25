def fibonacci_recursive_with_cache(n, cache={}):
    if n in cache:
        return cache[n]
    elif n <= 1:
        return n
    else:
        result = fibonacci_recursive_with_cache(n-1, cache) + fibonacci_recursive_with_cache(n-2, cache)
        cache[n] = result
        return result

print(fibonacci_recursive_with_cache(int(input())))