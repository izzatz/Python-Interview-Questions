# n = raw_input("ENTER  STRING\n")
n = "CAMMAC"
length = len(n)

for i in range(0, int(length/2 + 1)):
    if n[i] is not n[-i - 1]:      #change logic here.
        break

if i < (length / 2):
   print("not")
else:
   print("yes")