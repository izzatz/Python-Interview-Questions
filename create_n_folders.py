import os

i = 0
while i < 5:
  i += 1
  print(i)
  os.makedirs("aaa" + str(i))
