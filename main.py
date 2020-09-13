min = int(input("Minimum number: "))
max = int(input("Maximum number: "))
output = []
while min < max+1:
  if min%2 == 0:
    res = [int(x) for x in str(min)]
    if res[0] != res[1] and res[0] != res[2] and res[0] != res[3] and res[1] != res[2] and res[1] != res[3] and res[2] != res[3]:
      output.append(min)
  min+=1
print(output)
print(len(output))
