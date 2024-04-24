# Q.7
def display(a):
    if a%5==0:
        return True
    else:
        return False

def main():
    b=int(input("enter a number: "))
    
    print(display(b))
if __name__=="__main__":
    main()