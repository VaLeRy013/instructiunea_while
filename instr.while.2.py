t1=0
t2=0
t3=0
t4=0
t5=0
t6=0
tot=0
while tot<12:
    
    x=int(input(" temperatura: "))
    
    if(x<0):
        t3=x+t4
        t6=t6+1
        t4=t3
    elif(x>=0):
        t2=x+t1
        t5=t5+1
        t1=t2
    
    

    
    
    
    tot = tot +1
print(t3/t6)
print(t2/t5)