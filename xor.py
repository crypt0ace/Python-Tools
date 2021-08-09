#!/usr/bin/python3
s1 = input("Whats the first arg? (In HEX): ")
s2 = input("Whats the second arg? (In Binary): ")
h = hex(int(s1, 16) ^ int(s2, 16))[2:]
print(bytes.fromhex(h).decode('utf-8'))