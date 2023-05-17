def encrypt(text,key):
  cipher = ""
  for i in range(0,len(text)):
    if text[i].isalpha():
      cipher += chr((ord(text[i])+key) % 97 +97)
    elif text[i] == ' ':
      cipher += ' '
    else:
      cipher += chr((ord(text[i])+key) % 48 +48)
  return cipher

def decrypt(cipher,key):
  decipher = ""
  for i in range(0,len(cipher)):
    if cipher[i].isalpha():
      decipher += chr((ord(cipher[i]) - key) % 97 +97)
    elif cipher[i] == ' ':
      decipher += ' '
    else:
      decipher += chr((ord(cipher[i]) - key) % 48 +48)
  return decipher

text = input("enter text: ")
key = int(input("enter key: "))

key = key % 26

cipher = encrypt(text,key)
print(cipher)

decipher = decrypt(cipher,key)
print(decipher)