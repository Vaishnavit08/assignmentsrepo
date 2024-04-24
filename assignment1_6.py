# Q.6
def display(b):
    if b>0:
        print("positive") 
    elif b<0:
        print("negative")
    elif b==0:
        print("zero")
def main():
    a=int(input("enter a number = "))
    print(display(a))
if __name__=="__main__":
    main()