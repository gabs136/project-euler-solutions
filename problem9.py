trips=[]

def is_pit_trip(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else: 
        return False
    


for i in range(400,601):
    for a in range(0,i):
        b=i-a
        trips.append([a,b,(1000-a-b)])
        

for x in trips:
    if is_pit_trip(x[0],x[1],x[2])==True:
        print(x)
        