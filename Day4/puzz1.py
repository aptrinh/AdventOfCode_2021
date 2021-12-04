#-------------
#   Day 4.1/50
#-------------
def w(b):
 c,d,s=range,map,sum
 q=[[[*d(int, b[j+i].split())]for i in c(2,7)]for j in c(0,len(b)-1,6)]
 for m in [*d(int,b[0].split(','))]:
  for i,p in enumerate(q:=[[[n*(n!=m) for n in r]for r in p]for p in q]):
   if s(d(lambda x:any(s(r)==0 for r in x),[p,zip(*p)])):yield m*s(d(s,p));del q[i]
print((a:=[*w([*open("E:\Projects\Coding\AdventOfCode_2021\Day4\Day4Input.txt")])])[0],a[-1])



