def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print (f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Lets do some math with just functions")

age = add(40, 7)
heigt = subtract(200, 12)
weight = multiply(55, 2)
iq = divide(260, 2)

print(f"Age: {age}, Heigt: {heigt}, Weigt: {weight}, IQ {iq}")

print("Here is a puzzle")

what = add(age, subtract(heigt, multiply(weight, divide(iq, 2))))
print("Thats becomes: ", what, "Can I do  it by hand?")