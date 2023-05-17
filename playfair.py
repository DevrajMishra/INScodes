data ={}

def encrypt(text,mat):
  ans =""
  for i in range(0,len(text),2):
    a = data[text[i]]
    b = data[text[i+1]]
    if a[0] != b[0] and a[1] != b[1]:
      ans += mat[b[0]][a[1]] + mat[a[0]][b[1]]
    elif a[0] != b[0]:
      ans += mat[(a[0]+1)%5][a[1]] + mat[(b[0]+1)%5][a[1]]
    else:
      ans += mat[(a[0])][(a[1]+1)%5] + mat[a[0]][(b[1]+1)%5]
  return ans    

def decrypt(text,mat):
  ans =""
  for i in range(0,len(text),2):
    a = data[text[i]]
    b = data[text[i+1]]
    if a[0] != b[0] and a[1] != b[1]:
      ans += mat[b[0]][a[1]] + mat[a[0]][b[1]]
    elif a[0] != b[0]:
      ans += mat[(a[0]-1)%5][a[1]] + mat[(b[0]-1)%5][a[1]]
    else:
      ans += mat[(a[0])][(a[1]-1)%5] + mat[a[0]][(b[1]-1)%5]
  return ans        
    
def process_text(text):
  newt = ""
  i=0
  while i<(len(text)):
    if i<len(text)-1:
      if text[i] != text[i+1]:
        newt+= text[i] + text[i+1]
        i+=1
      else:
        newt+= text[i] + 'x'
    else:
      newt+= text[i] + 'x'
    i+=1
    
  if len(newt)%2 != 0:
    newt += 'x'*2
  return newt

def create_matrix(key):
  mat = [[None]*5 for i in range(5)]
  n = len(key)
  newk = ""
  
  for i in range(n):
    if newk.find(key[i]) == -1:
      newk += key[i]
  
  key = newk
  n = len(key)
 
  for i in range(n):
    mat[int(i/5)][i%5] = key[i]
    data[key[i]]=[int(i/5),i%5]
    
  k = n
  
  for i in range(0,26):
    if chr(97+i) == 'i':
      continue
    if key.find(chr(97+i)) == -1:
      mat[int(k/5)][k%5] = chr(97+i)
      data[chr(97+i)]=[int(k/5),k%5]
      k+=1
    if k == 25:
      break
  
  return mat

text = input("enter text: ")
key = input("enter key: ")

text = process_text(text)
mat = create_matrix(key)
cipher = encrypt(text,mat)
decipher = decrypt(cipher,mat)

# print(text)
# print(mat)
# print(data)
print(cipher)
print(decipher)

"""

jazz
morachy

m o r a c
h y b d e
f g i k l
n p q s t
u v w x z

"""