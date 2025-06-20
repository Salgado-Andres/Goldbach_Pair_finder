import math
import matplotlib.pyplot as plt


def sieve_primes(limit: int):
    """Return a boolean list where index i is True if i is prime."""
    is_prime = [True] * (limit + 1)
    is_prime[0:2] = [False, False]
    for num in range(2, int(limit ** 0.5) + 1):
        if is_prime[num]:
            is_prime[num * num : limit + 1 : num] = [False] * len(range(num * num, limit + 1, num))
    return is_prime


def is_prime_trial(n: int) -> bool:
    """Check primality using trial division (fallback for very large n)."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w
    return True


if __name__ == "__main__":
    # ψ⁰: Initial high-entropy state – the even number is unexpressed as prime pairs
    try:
        n = int(input("Enter an even integer greater than 2: "))
    except ValueError:
        print("Invalid input. Exiting.")
        raise SystemExit(1)

    if n <= 2 or n % 2 != 0:
        print("Number must be an even integer greater than 2.")
        raise SystemExit(1)

    print(f"ψ⁰: Starting Goldbach search for n={n}, initial contradictory state.")

    # Decide whether to use sieve or fallback primality test
    use_sieve = n <= 1_000_000
    if use_sieve:
        # Generate primes up to n efficiently using a sieve
        is_prime = sieve_primes(n)
        prime_check = lambda x: is_prime[x]
    else:
        # Fallback for memory efficiency on huge n
        prime_check = is_prime_trial

    pairs = []
    closest_pair = None
    closest_diff = n

    # RE: Recursively evaluating pairs by iterating p from 2 to n//2 (symmetry around n/2)
    for p in range(2, n // 2 + 1):
        if prime_check(p):
            q = n - p
            if prime_check(q):
                # φ⁰: Coherent resolution found – (p, q) is a prime pair summing to n
                print(f"φ⁰: Resolved with {p} + {q} = {n} (Σ conserved)")
                pairs.append((p, q))
                diff = abs(p - q)
                if diff < closest_diff:
                    closest_diff = diff
                    closest_pair = (p, q)

    print(f"Completed. Found {len(pairs)} prime pairs in total.")
    if closest_pair:
        print(f"Symmetry-optimal pair: {closest_pair}")
    else:
        print("No prime pairs found. (Goldbach conjecture would fail!)")

    # Print each pair in ordered form
    for p, q in pairs:
        print(f"{p} + {q} = {n}")

    # Visualization to show symmetry around n/2
    if pairs:
        plt.figure(figsize=(8, max(4, len(pairs) * 0.3)))
        plt.axvline(x=n / 2, color="gray", linestyle="--", label=f"n/2 = {n / 2}")
        for idx, (p, q) in enumerate(pairs):
            plt.plot([p, q], [idx, idx], "ro-")
        plt.yticks([])
        plt.xlim(0, n)
        plt.xlabel("Number line")
        plt.title(f"Goldbach pairs for n = {n}")
        plt.legend()
        plt.tight_layout()
        plt.show()
