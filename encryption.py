import hashlib
str = raw_input()
encoded = hashlib.sha256(str.encode())
print(encoded.hexdigest())

