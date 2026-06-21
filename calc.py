def calc():
    while True:
        print("two number calculator\n""press ctrl+c to exit\n")
        a= input("::")
        op= input("+-*/::")
        b=input("::")
        res=0
        if op=="+":
            res=float(a)+float(b)
            print(res)
        elif op =="-":
            res=float(a)-float(b)
            print(res)
        elif op=="/":
            res=float(a)/float(b)
            print(res)
        elif op=="*":
            res=float(a)*float(b)
            print(res)
        else:
            print("wrong input")
    
        
