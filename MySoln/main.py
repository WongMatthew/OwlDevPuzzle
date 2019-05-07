import base64
from caesarcipher import CaesarCipher

# ENCRYPTED is the original Hootsuite puzzle that bigger brother found on a Hootsuite USB
file = open("ENCRYPTED", "r") 
contents = file.read()

# Being tidy and closing the file object
file.close()

# Decodes ENCRYPTED file using base64
decoded = base64.b64decode(contents)

# Create list for the uppercase characters
upper_chars = []

# Find and add uppercase characters to list
for c in str(decoded):
  if c.isupper():
    upper_chars.append(c)

# Use the caeser cipher package to 
cipher = CaesarCipher(upper_chars)
print(cipher.cracked)