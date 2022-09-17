N = 32 #2147483647
quotient = N
bit = [] # Bit representation
while quotient != 0:
    remainder = quotient%2
    bit.append(remainder)
    quotient = quotient//2

if bit[0]==0:
    bit = bit[::-1]
print(bit)

# Not yet finished

