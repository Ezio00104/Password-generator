import random
import array
pass_len=int(input("enter the length of password must be greater than 4: "))
digits=['0','1','2','3','4','5','6','7','8','9']
small=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
big=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbol=['!','@','$','%','^','&','*','(',')','_','+','=',':',';','/','+']
comb_list= symbol + digits + small + big
rand_digits=random.choice(digits)
rand_small=random.choice(small)
rand_big=random.choice(big)
rand_symbol=random.choice(symbol)
x= rand_symbol+rand_digits+rand_big+rand_small
for i in range(pass_len-4):
    x=x+random.choice(comb_list)
    y=array.array('u',x)
    random.shuffle(y)
password=" "
for a in y:
   password=password+a
print(password) 
