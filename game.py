i=input('Wanna play tic tac toe \n yes or no:')
if i=='yes':
    print('so lets go!!')
    v=input('which character do u want,x or o?')
    n=v.lower()
    if n=='x':
        print('player1=',n)
        print('player2=o')
    elif n=='o':
        print('player1=o')
        print('player2=x')
elif i=='no':
    print('thank u')  
if i=='yes':

    Win = 1    

    Draw = -1    

    Running = 0    

    Stop = 1 
    board=['-','-','-',
           '-','-','-',
           '-','-','-']
    print(board[0],'I',board[1],'I',board[2])
    print('-----------')
    print(board[3],'I',board[4],'I',board[5])
    print('-----------')
    print(board[6],'I',board[7],'I',board[8])
    def CheckPosition(v):
        if(board[v] == ' '):

            return True
        else:
            return False    
    k=0
    while  k<9:
        i= int(input('player 1:select a spot:'))
        if v=='x':
            if board[i]!='x' and board[i]!='o':
                board[i]=v
                print(board[0],'I',board[1],'I',board[2])
                print('-----------')
                print(board[3],'I',board[4],'I',board[5])
                print('-----------')
                print(board[6],'I',board[7],'I',board[8])
                j=int(input('player2-select a spot:'))
                if board[j]!='x' and board[j]!='o':
                    board[j]='o'
                    print(board[0],'I',board[1],'I',board[2])
                    print('-----------')
                    print(board[3],'I',board[4],'I',board[5])
                    print('-----------')
                    print(board[6],'I',board[7],'I',board[8])
                    k=k+1
        else:
            if v=='o':
                if board[i]!='x' and board[i]!='o':
                    board[i]=v
                    print(board[0],'I',board[1],'I',board[2])
                    print('-----------')
                    print(board[3],'I',board[4],'I',board[5])
                    print('-----------')
                    print(board[6],'I',board[7],'I',board[8])
                    j=int(input('player2-select a spot'))
                    if board[j]!='x' and board[j]!='o':
                        board[j]='x'
                        print(board[0],'I',board[1],'I',board[2])
                        print('-----------')
                        print(board[3],'I',board[4],'I',board[5])
                        print('-----------')
                        print(board[6],'I',board[7],'I',board[8])
                        k=k+1
                                
