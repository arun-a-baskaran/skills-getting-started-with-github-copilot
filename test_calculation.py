#Create a python function to generate a fibanocci series up to a given number n
def fibonacci_up_to_n(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
#Test the function with n = 10
print(fibonacci_up_to_n(10))