# Q. ANSWER
def display(no):
    if no%2==0:
        print("even")
    else:
        print("odd")

def chknum():
    a=int(input("enter a number  = "))
    display(a)

if __name__=="__main__":
    chknum()