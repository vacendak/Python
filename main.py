import time


# Function to calculate PI with a given number of decimals
def calculate_pi_decimals(tot):
    k = 4000
    t = 1000

    if tot % 3 != 0:
        tot += 1

    print("\n\n\tPI = 3,", end="")

    num = (tot // 3) + 3
    a = [0] * 1000000

    start_time = time.time()  # Start timing

    while k > 1:
        k -= 1
        q = 0

        a[0] += 2
        p = 1 + 2 * k

        for j in range(num):
            if (j > 2 and k == 1) or k == 0:
                d = a[j - 2] % t + (q // p) // t
                print(f"{d:03d}", end="")
            q = a[j] * k + q % p * t
            a[j] = q // p

    end_time = time.time()  # End timing
    execution_time = end_time - start_time  # Calculate execution time

    tot = (num - 3) * 3

    print(f"\n\n\tOutput number of decimals: {tot}")
    print(f"\n\tExecution time: {execution_time:.6f} seconds")
    print("\n")


if __name__ == "__main__":
    while True:
        tot = int(input("\n\nEnteer the desired number of decimals:  "))
        calculate_pi_decimals(tot)

        otro = input("\n\tTry again? (y/n): ")
        if otro.lower() != 'y':
            break

    print("\n\n")
