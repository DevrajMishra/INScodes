def encrypt(text,key):  
  if len(text) % 2 != 0:
    n = len(text) - len(text) % 2
    text+= '#'*n
    
  cipher = ""
  for i in range(0,len(text),2):
    a = int(ord(text[i])-97)
    b = int(ord(text[i+1])-97)
    
    t = (key[0][0] * a + key[0][1] * b)%26+97
    cipher += chr(t)
    
    t = (key[1][0] * a + key[1][1] * b)%26+97
    cipher += chr(t)
    
  return cipher

def inverse_det(det):
  for i in range(26):
    if (det*i) % 26 == 1:
      return i

def decrypt(text,key):
  det = key[0][0] * key[1][1] - key[1][0] * key [0][1]
  invdet = inverse_det(det)
  key[0][0] , key[1][1] = key[1][1] , key[0][0]
  key[0][1] = invdet * (- key[0][1])
  key[1][0] = invdet * (- key[1][0])
  key[0][0] = invdet * (key[0][0])
  key[1][1] = invdet * (key[1][1])
  
  decipher = ""
  for i in range(0,len(text),2):
    a = int(ord(text[i])-97)
    b = int(ord(text[i+1])-97)
    
    t = (key[0][0] * a + key[0][1] * b)%26+97
    decipher += chr(t)
    
    t = (key[1][0] * a + key[1][1] * b)%26+97
    decipher += chr(t)
  return decipher

text = input("enter text: ")
print("enter key: ")

key = [[0]*2 for i in range(2)]

for i in range(0,2):
  for j in range(0,2):
    key[i][j]=(int(input()))

cipher = encrypt(text,key)
print(cipher)

decipher = decrypt(cipher,key)
print(decipher)

#key 
#3
#4
#2
#5