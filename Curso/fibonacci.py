n=max(int(input('¿Cuántos valores quieres? (minimo 5)')),5)
old=0
x=1
print(old)
print(x)
for i in range(0,n-2):
  y=x+old
  print(y)
  old=x
  x=y


while True:
  n=int(input('¿Cuántos valores quieres? (mínimo 3)'))
  if n > 2:
    break
x=[0,1]
for i in range(n-2):
  x.append(x[-1]+x[-2])
print(x)


lista=[0,1]
for i in range(3,21):
  lista.append(lista[len(lista)-1]+lista[len(lista)-2])
print(list(lista))


def fibo(n):
  a=0
  b=1
  for i in range(3,n+1):
    c=a+b
    a=b
    b=c
  return(c)
print(fibo(100))


fibo=[0,1]
for i in range (50):
  fibo.append(fibo[-1]+fibo[-2])
print(fibo)


def fibo(n):
  a,b=0,1
  for i in range(n):
    print(a,end=' ')
    a,b=b,a+b
  print()
fibo(15)