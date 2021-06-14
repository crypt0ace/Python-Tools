#!/usr/bin/env python3
import hashlib
str = input("Enter The String To Encode: ")
enc = hashlib.md5(str.encode('utf-8')).hexdigest()
print("MD5 HASHED: " + enc)