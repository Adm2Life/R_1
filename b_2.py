#Bubble Sort 

ar = [8,5,3,6,1,9,4]

for x in range(len(ar)):
 for y in range(len(ar)-1):
  if ar[y]>ar[y+1] : 
   ar[y] , ar[y+1] = ar[y+1] , ar[y]

print("Ar after sorting == ", ar)