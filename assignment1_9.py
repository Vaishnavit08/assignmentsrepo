# Q . 9

def display(b):
    c=0
    for i in range(0,2*b,2):
        print(i)
        c+=1
    return c 
def main():
    a=int(input("enter a number = "))
    print(display(a))

if __name__=="__main__":
    main()