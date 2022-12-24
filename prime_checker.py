def prime_checker(number):
    # Initialize a flag to indicate whether the number is prime
    is_prime = True

    # Iterate through the range 2 to number ...n
    for i in range(2, number):
        # If the number is divisible by any of the values in the range, it is not prime
        if number % i == 0:
            is_prime = False
    # If the number is prime, print a message to the user
    if is_prime:
        print("It's a prime number.")
    # If the number is not prime, print a message to the user
    else:
        print("It's not a prime number.")


# Prompt the user to enter a number
n = int(input("Check this number: "))

# Check if the number is prime
prime_checker(number=n)
