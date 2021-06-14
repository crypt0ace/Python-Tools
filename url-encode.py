#!/usr/bin/env python3
import urllib.parse
str = input("Enter The String To Encode: ")
enc = urllib.parse.quote_plus(str)
print("URL Encoded: " + enc)