import threading
import time
from math import isqrt

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

# Function to count prime numbers in a given range
def count_primes_in_range(start, end):
    count = 0
    for number in range(start, end):
        if is_prime(number):
            count += 1
    return count

# Function to run the prime counting in multiple threads
def run_with_threads(num_threads, start, end):
    threads = []
    range_per_thread = (end - start) // num_threads
    results = [0] * num_threads

    # Create and start threads
    for i in range(num_threads):
        thread_start = start + i * range_per_thread
        thread_end = start + (i + 1) * range_per_thread
        t = threading.Thread(target=lambda idx: results.__setitem__(idx, count_primes_in_range(thread_start, thread_end)), args=(i,))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    # Combine results from all threads
    total_primes = sum(results)
    return total_primes

if __name__ == '__main__':
    start_range = 1
    end_range = 100000
    num_threads = 4  # Number of threads to use

    # Measure execution time
    start_time = time.time()
    prime_count = run_with_threads(num_threads, start_range, end_range)
    end_time = time.time()

    print(f"Number of primes found: {prime_count}")
    print(f"Execution time: {end_time - start_time:.2f} seconds")
