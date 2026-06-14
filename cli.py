def calc():
    a=int(input("a"))
    b=int(input("b"))
    print(a+ b)
def main():
    menu={"calculator":"calc",}
    
    print( "The meo at you srvice ""\nmenu for menu" )
    
        
    while True:
        cmd=input("hukum::")
        if cmd=="menu":
            for k,v in menu.items():
                print(f"{k}--{v}")
        if cmd=="calc":
            calc()
            
main()