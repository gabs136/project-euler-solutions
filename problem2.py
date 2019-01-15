current_term =2
last_term = 1
aux =0
soma =2
print(last_term)
print(current_term)
while True:
    aux = current_term
    current_term += last_term
    last_term = aux
    if current_term >= 4000000:
       break
    if current_term%2 == 0:
        soma += current_term
    print(current_term)

print(soma)
