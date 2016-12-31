min = 200 #Escribir a partir de que numero se comienzara
max = 300 #Escribir hasta que numero se terminara
R = range(min, (max+1))
s = 0 #+1 si la division tiene un cociente igual a 0
c = 1 #

for n in R:
  
  while c <= max:
  
    if n%c == 0:
      s += 1
    
    c += 1
    
  if s == 2:
    print(n, "Es primo")
  
  s = 0
  c = 1
