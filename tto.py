import random
print("1 - single player mode")
print("2 - two player mode")
print("3 - exit :(")

x = int(input("choose what you want?"))
while True:
    if x == 1:
        def show():
            for i in range(0, 9):
                print(game[i], end=' ')
                if i == 2 or i == 5:
                    print()
            print()


        def check():
            b = False

            # -----------------row  system------------------------------
            if game[0] == 'x' and game[1] == 'x' and game[2] == 'x':
                print('winner is system')
                b = True

            if game[3] == 'x' and game[4] == 'x' and game[5] == 'x':
                print('winner is system')
                b = True

            if game[6] == 'x' and game[7] == 'x' and game[8] == 'x':
                print('winner is system')
                b = True

            # -----------------row  you------------------------------
            if game[0] == 'o' and game[1] == 'o' and game[2] == 'o':
                print('winner is o')
                b = True

            if game[3] == 'o' and game[4] == 'o' and game[5] == 'o':
                print('winner is o')
                b = True

            if game[6] == 'o' and game[7] == 'o' and game[8] == 'o':
                print('winner is o')
                b = True

            # -----------------col  you------------------------------
            if game[0] == 'o' and game[3] == 'o' and game[6] == 'o':
                print('winner is o')
                b = True

            if game[1] == 'o' and game[4] == 'o' and game[7] == 'o':
                print('winner is o')
                b = True

            if game[2] == 'o' and game[5] == 'o' and game[8] == 'o':
                print('winner is o')
                b = True

            # -----------------col  system------------------------------
            if game[0] == 'x' and game[3] == 'x' and game[6] == 'x':
                print('winner is system')
                b = True

            if game[1] == 'x' and game[4] == 'x' and game[7] == 'x':
                print('winner is system')
                b = True

            if game[2] == 'x' and game[5] == 'x' and game[8] == 'x':
                print('winner is system')
                b = True

            # -----------------ghotr  system------------------------------
            if game[0] == 'x' and game[4] == 'x' and game[8] == 'x':
                print('winner is system')
                b = True


            if game[2] == 'x' and game[4] == 'x' and game[6] == 'x':
                print('winner is system')
                b = True

            # -----------------ghotr  you------------------------------
            if game[0] == 'o' and game[4] == 'o' and game[8] == 'o':
                print('winner is o')
                b = True

            if game[2] == 'o' and game[4] == 'o' and game[6] == 'o':
                print('winner is o')
                b = True


            if game.count('-') == 0:
                print('draw :( ')
                b = True

            return b


        # -----------------------------------------------
        game = []
        for i in range(0, 9):
            game.append('-')
        # -----------------------------------------------
        # show()
        # ------------------------------------------------
        print('-' * 20)
        # -----------------------------------------------
        while True:
            if check():
                break
            while True:
                s = random.randint(0, 8)
                if game[s] == '-':
                    game[s] = 'x'
                    break
            show()
            print('-' * 20)
        # -----------------------------------------------
            if check():
                break
            s = int(input('o  => num (0 ..8 ) :'))
            if game[s] == '-':
                game[s] = 'o'
            show()
            print('-' * 20)
        s = int(input('0  => exit\n1 => another match\nchoose:'))
        if s == 1:
            continue
        elif s == 0:
            print("over")
            break
    elif x == 2:

        def show():
            for i in range(0, 9):
                print(game[i], end=' ')
                if i == 2 or i == 5:
                    print()
            print()


        def check():
            b = False
            # -----------------row  system------------------------------
            if game[0] == 'x' and game[1] == 'x' and game[2] == 'x':
                print('winner is x')
                b = True

            if game[3] == 'x' and game[4] == 'x' and game[5] == 'x':
                print('winner is x')
                b = True

            if game[6] == 'x' and game[7] == 'x' and game[8] == 'x':
                print('winner is x')
                b = True

            # -----------------row  you------------------------------
            if game[0] == 'o' and game[1] == 'o' and game[2] == 'o':
                print('winner is o')
                b = True

            if game[3] == 'o' and game[4] == 'o' and game[5] == 'o':
                print('winner is o')
                b = True

            if game[6] == 'o' and game[7] == 'o' and game[8] == 'o':
                print('winner is o')
                b = True

            # -----------------col  you------------------------------
            if game[0] == 'o' and game[3] == 'o' and game[6] == 'o':
                print('winner is o')
                b = True

            if game[1] == 'o' and game[4] == 'o' and game[7] == 'o':
                print('winner is o')
                b = True

            if game[2] == 'o' and game[5] == 'o' and game[8] == 'o':
                print('winner is o')
                b = True

            # -----------------col  system------------------------------
            if game[0] == 'x' and game[3] == 'x' and game[6] == 'x':
                print('winner is x')
                b = True

            if game[1] == 'x' and game[4] == 'x' and game[7] == 'x':
                print('winner is x')
                b = True

            if game[2] == 'x' and game[5] == 'x' and game[8] == 'x':
                print('winner is x')
                b = True

            # -----------------ghotr  system------------------------------
            if game[0] == 'x' and game[4] == 'x' and game[8] == 'x':
                print('winner is x')
                b = True


            if game[2] == 'x' and game[4] == 'x' and game[6] == 'x':
                print('winner is x')
                b = True

            # -----------------ghotr  you------------------------------
            if game[0] == 'o' and game[4] == 'o' and game[8] == 'o':
                print('winner is o')
                b = True

            if game[2] == 'o' and game[4] == 'o' and game[6] == 'o':
                print('winner is o')
                b = True

            if game.count('-') == 0:
                print('draw :( ')
                b = True

            return b


        # -----------------------------------------------
        game = []
        for i in range(0, 9):
            game.append('-')
        # -----------------------------------------------
        show()
        print('-' * 20)
        # -----------------------------------------------
        while True:

            if check()==True:
                break
            s = int(input('x  => num (0 ..8 ) :'))
            if game[s] == '-':
                game[s] = 'x'
            show()
            print('-' * 20)
            # -----------------------------------------------
            if check()==True:
                break
            s = int(input('o  => num (0 ..8 ) :'))
            if game[s] == '-':
                game[s] = 'o'
            show()
            print('-' * 20)
        s = int(input('0  => exit\n1 => another match\nchoose:'))
        if s == 1:
            continue
        elif s == 0:
            print("over")
            break
    elif x == 3:
        break
