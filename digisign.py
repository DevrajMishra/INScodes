import math
import hashlib

def rsa_keys():
  p = 53
  q = 59
  n = p*q
  phin = (p-1)*(q-1)
  e = 0
  for i in range(2,phin):
    if math.gcd(i,phin) == 1:
      e = i
      break

  d = 0
  for k in range(1,phin):
    d = (1 + k*phin)/e
    if d == int(d):
      d = int(d)
      break
  return e,d,n

text = b"hello"
e,d,n = rsa_keys()

hashed = hashlib.sha256(text).hexdigest()
hashed_int = int(hashed, 16) % n
signature = pow(hashed_int, d, n)


hashed = hashlib.sha256(text).hexdigest()
hashed_int = int(hashed, 16) % n
hash_ans = pow(signature, e, n)

print(hashed_int,hash_ans)


# 53
# 59