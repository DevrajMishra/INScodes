import math

def find_d(e,phi_n,q):
  for k in range(1,phi_n):
    temp=(1+k*phi_n)/e
    int_temp=int(temp)
    if temp==int_temp:
      return int_temp
  
def find_e(phi_n):
  for i in range(2,phi_n):
    if math.gcd(i,phi_n) == 1:
      return i

def preprocess(p,q):
  n=p*q
  phi_n=(p-1)*(q-1)
  e=find_e(phi_n)
  d=find_d(e,phi_n,q)
  print('e: ',e,' d: ',d)
  return e,d,n
  
def decrypt_rsa(d,n,cipher):
  decipher=pow(cipher,d)%n
  print('decipher: ',decipher)
  return decipher
  
def encrypt_rsa(e,n,plain):
  cipher=pow(plain,e)%n
  print('cipher: ',cipher)
  return cipher
  
p=int(input('enter p:'))
q=int(input('enter q:'))
e,d,n=preprocess(p,q)
plain = int(input('enter plain text:'))
cipher=encrypt_rsa(e,n,plain)
decipher=decrypt_rsa(d,n,cipher)


# 53
# 59