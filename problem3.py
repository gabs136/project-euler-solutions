numdiv=[]
primediv=[]
largest = 0
greatest=0

def is_prime(num):
        dlist=[]
        for j in range(1,num):
                if num%j==0:
                        dlist.append(j)
           
        if len(dlist) == 1:
                result = True
        else:
                result = False        

        return result               




numb=600851475143 



for i in range(1,numb ):
        if numb %i==0:
                numdiv.append(i)
                print(i)

print("ALL DIVS FOUND ALL DIVS FOUND ALL DIVS FOUND ALL DIVS FOUND ALL DIVS FOUND ")


for x in numdiv:  
        if is_prime(x)==True:
                primediv.append(x)

print(primediv[-1])

