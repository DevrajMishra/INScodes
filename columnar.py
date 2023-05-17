def encrypt(text,columns):
  if len(text) % columns != 0:
    n =  columns - len(text) % columns
    text += '#'*n
  cipher = ""
  
  for i in range(0,columns):
    for j in range(i,len(text),columns):
      cipher += text[j]
      
  for i in range(0,len(text)):
    if i % columns == 0:
      print()
    print(text[i],end=' ')
  print()
  
  return cipher

def decrypt(text,columns):
  columns = int(len(text)/columns)
  decipher = ""
  for i in range(0,columns):
    for j in range(i,len(text),columns):
      decipher += text[j]
      
  for i in range(0,len(text)):
    if i % columns == 0:
      print()
    print(text[i],end=' ')
  print()
  
  ans = ""
  for i in range(0,len(decipher)):
    if decipher[i]!="#":
      ans+=decipher[i]
  return ans

text = input("enter text: ")
columns = int(input("columns: "))

cipher = encrypt(text,columns)
print(cipher)

decipher = decrypt(cipher,columns)
print(decipher)



# djsanghvi
'''
d j s a
n g h v
i # # #




'''