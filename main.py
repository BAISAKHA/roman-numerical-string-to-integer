s=input()
sum=0
for i in s:
  if (i=='I'):
    sum+=1
  elif (i=='V'):
        sum+=5
  elif (i=='X'):
        sum+=10
  elif (i=='L'):
        sum+=50
  elif (i=='C'):
        sum+=100
  elif (i=='D'):
        sum+=500
  elif (i=='M'):
        sum+=1000

if "XL" in s:
  sum=sum-60+40
elif "IX" in s:
  sum=sum-11+9
elif "XC" in s:
  sum=sum-110+90
elif "CD" in s:
  sum=sum-600+400
elif "CM" in s:
  sum=sum-1100+900


print(sum)
  
    
  