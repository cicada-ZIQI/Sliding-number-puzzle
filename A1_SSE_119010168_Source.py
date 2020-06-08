import random

#global variable
list,list2,direction=[],[],[]
l,r,u,d,instruction="","","","",""

#output:three rows, three columns
def output(number):
    if number == 9:
        print(list[0],"\t",list[1],"\t",list[2],"\n",list[3],"\t",list[4],"\t",list[5],
        "\n",list[6],"\t",list[7],"\t",list[8],sep="") 
    if number == 16:
        print(list[0],"\t",list[1],"\t",list[2],"\t",list[3],"\n",list[4],"\t",
        list[5],"\t",list[6],"\t",list[7],"\n",list[8],"\t",list[9],"\t",list[10],
        "\t",list[11],"\n",list[12],"\t",list[13],"\t",list[14],"\t",list[15],sep="")

#produce a sovable 9-puzzle
def produce_9number():
    global list,list2
    while True:
        list=[1,2,3,4,5,6,7,8," "]
        list2=[]
        random.shuffle(list)
        #to make sure it is solvable, the inverse number must be even
        inverse_number=0
        for i in list:
            list2.append(i)
        list2.remove(" ")
        for n in range(7):
            for i in range(n+1,8):
                if list2[n] > list2[i]:
                    inverse_number += 1
        if inverse_number%2 == 0:
            output(9)
            return list 
        #if the inverse number is odd, then reproduce the puzzle
        else:
            continue

#ask user to prompt direction instructions
def order():
    global l,r,u,d,direction
    while True:
        direction=[]
        try:
            directions=input("enter four letters used to represent left, right, up and down:") 
            for i in directions:
                if i !=" "and i!=",":
                    direction.append(i)
            l,r,u,d=direction 
            if l != r != u != d:
                break
            else:
                continue   
        except:
            continue           

#tell the computer how to move            
def move(p_number, p_puzzle_number):
    for i in range(p_puzzle_number):
        if list[i] == " ":
            a=i
    if instruction == l:
        list[a],list[a+1]=list[a+1],list[a]
        output(p_puzzle_number)
    if instruction==r:
        list[a],list[a-1]=list[a-1],list[a]
        output(p_puzzle_number)
    if instruction==u:
        list[a],list[a+p_number]=list[a+p_number],list[a]
        output(p_puzzle_number)
    if instruction==d:
        list[a],list[a-p_number]=list[a-p_number],list[a]
        output(p_puzzle_number)

#ask the user to prompt how to move and display the updated puzzle
def instruction_move_9():
    global instruction
    step=0
    while True:
        if list[0] == " ":
            instruction=input("Enter your move(left-"+l+","+"up-"+u+")")
            if instruction == d or instruction == r:
                continue
        if list[1] == " ":
            instruction=input("Enter your move(left-"+l+","+"up-"+u+","+"right-"+r+")")
            if instruction == d:
                continue
        if list[2] == " ":
            instruction=input("Enter your move(right-"+r+","+"up-"+u+")")
            if instruction == d or instruction == l:
                continue
        if list[3] == " ":
            instruction=input("Enter your move(left-"+l+","+"up-"+u+","+"down-"+d+")")
            if instruction == r:
                continue
        if list[4] == " ":
            instruction=input("Enter your move(left-"+l+","+"right-"+r+","+"up-"+u+","+"down-"+d+")")
        if list[5] == " ":
            instruction=input("Enter your move(right-"+r+","+"up-"+u+","+"down-"+d+")")
            if instruction == l:
                continue
        if list[6] == " ":
            instruction=input("Enter your move(left-"+l+","+"down-"+d+")")
            if instruction == r or instruction == u:
                continue 
        if list[7 ]== " ":
            instruction=input("Enter your move(right-"+r+","+"left-"+l+","+"down-"+d+")")
            if instruction == u:
                continue
        if list[8] == " ":
            if list == [1,2,3,4,5,6,7,8," "]:
                print("Congratulations!","You solved the puzzle in",step,"moves!")
                break
            else:
                instruction=input("Enter your move(right-"+r+","+"down-"+d+")")
                if instruction == l or instruction == u:
                    continue 
        move(3,9)
        step += 1

#all the fuctions need in 9-puzzle game
def main_play_9():
    order() 
    produce_9number()
    instruction_move_9()     

#produce a solvable 16-puzzle       
def produce_16number():
    global list,list2
    while True:
        list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15," "]
        list2=[]
        random.shuffle(list)
        inverse_number=0
        for i in list:
            list2.append(i)
        list2.remove(" ")
        #calculate the inverse number
        for n in range(14):
            for i in range(n+1,15):
                if list2[n] > list2[i]:
                    inverse_number+=1
        for i in range(16):
            if list[i] == " ":
                a=i                                  #a is where the white space initially at 
        if inverse_number%2 == 0:
            if (15-a)//4 == 0 or (15-a)//4 == 2:     #If inverse number is even, the diffenrence between the row where the  
                output(16)                           #white space initially at and the last row must be even.
                break
            else:
                continue
        else:
            if (15-a)//4 == 1 or (15-a)//4 == 3:     #If inverse number is odd the diffenrence between the row where the  
                output(16)                           #white space initially at and the last row must be odd.
                break
            else:
                continue

#ask the user to input how to move and update the 16-puzzle   
def instruction_move_16():
    global instruction,list2
    step=0
    while True:
        if list[0] == " ":
            instruction=input("Enter your move(left-"+l+","+"up-"+u+")")
            if instruction == d or instruction == r:
                continue
        if list[1] == " " or list[2] == " ":
            instruction=input("Enter your move(left-"+l+","+"up-"+u+","+"right-"+r+")")
            if instruction == d:
                continue
        if list[3] == " ":
            instruction=input("Enter your move(right-"+r+","+"up-"+u+")")
            if instruction == d or instruction == l:
                continue
        if list[4] == " "or list[8] == " ":
            instruction=input("Enter your move(left-"+l+","+"up-"+u+","+"down-"+d+")")
            if instruction == r:
                continue
        if list[5] == " " or list[6] == " " or list[9] == " " or list[10] == " ":
            instruction=input("Enter your move(left-"+l+","+"right-"+r+","+"up-"+u+","+"down-"+d+")")
        
        if list[7] == " " or list[11] == " ":
            instruction=input("Enter your move(right-"+r+","+"up-"+u+","+"down-"+d+")")
            if instruction == l:
                continue
        if list[12] == " ":
            instruction=input("Enter your move(left-"+l+","+"down-"+d+")")
            if instruction == r or instruction == u:
                continue 
        if list[13] == " " or list[14] == " ":
            instruction=input("Enter your move(right-"+r+","+"left-"+l+","+"down-"+d+")")
            if instruction == u:
                continue
        if list[15] == " ":
            list2.sort
            if list == list2+[" "]:
                print("Congratulations!","You solved the puzzle in",step,"moves!")
                break
            else:
                instruction=input("Enter your move(right-"+r+","+"down-"+d+")")
                if instruction == l or instruction == u:
                    continue 
        move(4, 16)
        step+=1

#all the fuctions need in 16-puzzle
def main_play_16():
    order() 
    produce_16number()
    instruction_move_16()  

#ask the user play which puzzle or quit the game
def main():
    print('''
Welcome to 8/15-puzzle game. You need to repeatedly slide an adjacent tile, one at a time, to
the currently unoccupied space until all numbers appear sequentially, ordered from left to right, 
top to bottom.
    ''')
    while True:
        game=input("Enter '1' for 8-puzzle, '2' for 15-puzzle or 'q' to end the game:")
        if game == "1":
            main_play_9()
        if game == "2":
            main_play_16()
        if game == "q":
            print("The game is end. Welcome back.")
            break
        else:
            continue
main()

