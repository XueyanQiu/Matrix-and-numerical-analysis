import matplotlib.pyplot as plt
import math


def compute_function_value(x):
    return 2*(math.e)**(-x)-math.sin(x)


def zero_theorem(x1,x2):
    r=(compute_function_value(x1)*compute_function_value(x2))
    if(r<=0):
        return True
    else:
        return False

def dichotomy(a,b,cache_x,epslion):
    k=0
    mid=(a+b)/2.0
    while((b-a)>=epslion or k==0):
     
        cache_x.append(mid)
        if(compute_function_value(mid)*compute_function_value(b)<0):
            a=mid
        else:
            b=mid
       
        print(k,mid,compute_function_value(mid))
        mid=(a+b)/2.0
        k=k+1
        
    return mid



def main():
    cache_x=[] 
    a=float(input("Please enter the left interval a:")) 
    b=float(input("Please enter the left interval b:")) 
  
    if(zero_theorem(a,b)):
        epslion=float(input("please enter the epslion:"))  
        x1=dichotomy(a,b,cache_x,epslion)
        plt.plot(cache_x,'or')
        plt.show()
        print('approximate solutions:',x1)
    else: 
        print('The equation has no root in the interval')

if __name__=='__main__':
    main()


        
        
