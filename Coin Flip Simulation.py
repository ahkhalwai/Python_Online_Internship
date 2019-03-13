import random

s=int(input('Enter the number of times you want to toss the coin: '))
n=0
tosses=[]
while n<s:
    t=random.randint(0,1)
    n+=1
    if t==1:
        t='H'
    else:
        t='T'
    tosses.append(t)    

print(f'Outcome of the tosses: {tosses}')
print(f'Number of Heads: {tosses.count("H")}')
print(f'Number of Tails: {tosses.count("T")}')
