def fibonacci_iterative(n):
    sequence = []
    for i in range(n):
        if i == 0:
            sequence.append(0)
        elif i == 1:
            sequence.append(1)
        else:
            sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

def fibonacci_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)



n = int(input("Enter the Number:"))  # Change this value for a different length of the sequence
print("Iterative Fibonacci sequence:")
fib_sequence = fibonacci_iterative(n)
for num in fib_sequence:
    print(num)

print("Recursive Fibonacci sequence:")
for i in range(n): 
    print(fibonacci_recursive(i)) 



