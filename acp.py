def reverse_bits(n):
    result = 0
    while n > 0:
        result <<= 1            
        result |= (n & 1)       
        n >>= 1                 
    return result

# Input from user
num = int(input("Enter your original number: "))
binary = bin(num)[2:]
print(f"({binary})")
reversed_num = reverse_bits(num)

# Output
print("Reversed Number:", reversed_num)
binary = bin(reversed_num)[2:]
print(f"({binary})")