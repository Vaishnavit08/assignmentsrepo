# Q. 8
def display(a):
    i=0
    while i<a:
        print("*",end=" ") 
        i+=1
def main():
    b=int(input("enter a number = "))
    print(display(b))
if __name__=="__main__":
    main()