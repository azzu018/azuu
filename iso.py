def sh(q,b):
  if(len(q)==len(b)):
    return("yes")
  else:
   return("no")
q,b=map(str,input().split())
print(sh(q,b))
