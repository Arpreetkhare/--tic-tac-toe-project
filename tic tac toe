def sum(a,b,c):
    return a+b+c

def printboard(xpos,ypos):

    zero= 'x'if xpos[0] else ('o' if ypos[0] else 0)
    one= 'x'if xpos[1] else ('o' if ypos[1] else 1)
    two= 'x'if xpos[2] else ('o' if ypos[2] else 2)
    three='x'if xpos[3] else ('o' if ypos[3] else 3)
    four= 'x'if xpos[4] else ('o' if ypos[4] else 4)
    five= 'x'if xpos[5] else ('o' if ypos[5] else 5)
    six= 'x'if xpos[6] else( 'o' if ypos[6] else 6)
    seven= 'x'if xpos[7] else ('o' if ypos[7] else 7)
    eight= 'x'if xpos[8] else ('o' if ypos[8] else 8)


    print(f' {zero} | {one} | {two} ')
    print(f"------------")
    print(f' {three} | {four} | {five} ')
    print(f"------------")
    print(f' {six} | {seven} | {eight} ')



def cheakwin(xpos,ypos):
    win= [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in win :
        if (sum(xpos[i[0]],xpos[i[1]],xpos[i[2]])==3):
            
            print("'x' won")
            return 1
        
            
        
        elif (sum(ypos[i[0]],ypos[i[1]],ypos[i[2]])==3):
                print("'o' won")
                return 0
                
                
        
    return -1 
            
            
        
            
xpos=[0,0,0,0,0,0,0,0,0]
ypos=[0,0,0,0,0,0,0,0,0]
turn =1
print('welcome to tic tac toe')
while(True):
    printboard(xpos,ypos)
    if turn ==1:
        print("X's chance")
        value=int(input("enter a value"))
        xpos[value]=1

    else:
        print("o's turn")
        value=int(input("enter a value"))
        ypos[value]=1
        
    cheaking=cheakwin(xpos,ypos)
    if cheaking!= -1:
        print("match over")
        break
    

    turn = 1-turn     
       



