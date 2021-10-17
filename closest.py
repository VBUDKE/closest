def closest(array,target,count):
 a=[]
 target=int()
 c=int(count)
 k=0
 p=len(array)-1
 if (len(array)-1<c):
  return array
 else:
  while(array[k]!=target)and(k!=p):
   g=(k+p) // 2
   d=array[g]
   if (target>d):
    k=g+1
   else:
    p=p-1
  c=c-1
  a.append(array[g])
  while (c>0):
   if (0==k):
    p=p+1
    a.append(array[p])
    c=c-1
   elif (len(array)-1==p):
    k=k-1
    a.insert(0,array[k])
    print(a)
    c=c-1
   else:
    c=c-1
    if (abs(target-array[k+1])<abs(target-array[d-1])):
     k=k-1
     a.insert(0,array)
    else:
     p=p+1
     a.append(array[p])
  return a
