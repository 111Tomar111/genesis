import random

while True:
    mode= int(input("best of 3/best of 5::"))
    options=["stone","scissor","paper"]
    ascore=0
    pscore=0
    if mode==3:
        while True:
            if pscore==3 or pscore==2 or ascore==3 or ascore==2:
                break
            aic=random.choice(options)
            pyc=input("go::")
            print(aic)
            if pyc==aic:
                print("same choice go again")
                continue
            elif aic=="paper" and pyc=="stone" or aic=="stone" and  pyc=="scissor" or aic=="scissor" and pyc=="paper":
                print("ai won this round")
                ascore+=1
                continue
            elif pyc=="paper" and aic=="stone" or pyc=="stone" and  aic=="scissor" or pyc=="scissor" and aic=="paper":
                print("player won this round")
                pscore+=1
                continue
    print(f"player score::{pscore}\nai score::{ascore}")
    if pscore>ascore:
        print("player won this match")
    if pscore<ascore:
        print("ai won this match")

    cont=input("wish to play again?(y/n)::")
    if cont=="y":
        continue
    elif cont=="n":
        break