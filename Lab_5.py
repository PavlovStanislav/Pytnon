from random import randint
import time
 

def dice_throw():
    plr1_pts=0
    plr2_pts=0
    a = str(input("Input player 1 name: "))
    b = str(input("Input player 2 name: "))
    plr1=a[:]
    plr2=b[:]
    print(a)
    print(b)
    
    for i in range(1,6):   
        print("Next run, number: ", i)
        print(plr1,'`s turn now')
        time.sleep(2)
        n1 = randint(1, 6)
        print('Number is: ', n1)

        print(plr2,'`s turn now')
        time.sleep(2)
        n2 = randint(1, 6)
        print('Number is: ', n2)

        if n1 > n2:
            print(plr1, 'wins.')
            plr1_pts+=1
        elif n1 < n2:
            print(plr2, 'wins.')
            plr2_pts+=1
        else:
            print('Draw')
            plr1_pts+=0.5
            plr1_pts+=0.5
    if plr1_pts>plr2_pts:
        print(plr1 + ' Wins. '+ " Points: "+ str(plr1_pts))
    elif plr1_pts<plr2_pts:
        print(plr2 + ' Wins. '+ " Points: " + str(plr2_pts))
    else:
        print('Draw: ', plr1_pts, "+",plr2_pts);

b = dice_throw();


