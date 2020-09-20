p1={0:"rock", 1:"paper", 2:"scissor"}
p2={5:"rock", 7:"scissor", 6:"paper"}

ch1=(input("Player 1, Enter your string of values: "))
bit1=int(input("Player 1, Enter your bit: "))
for i in range(0,len(ch1)):
    if(ch1[i]==ch1[bit1]):
        k1=int(ch1[i])
        break
    
ch2=input("Player 2, Enter your string of values: ")
bit2=int(input("Player 2, Enter your position of bit: "))
for i in range(0,len(ch2)):
    if(ch2[i]==ch2[bit2]):
        k2=int(ch2[i])
        break

if(p1[k1]==p2[k2]):
    print("Match is drawn.")
elif(p1[k1]=="rock" and p2[k2]=="scissor"):
    print("Player 1 wins,")
elif(p1[k1]=="rock" and p2[k2]=="paper"):
    print("Player 2 wins,")
elif(p1[k1]=="paper" and p2[k2]=="rock"):
    print("Player 2 wins,")
elif(p1[k1]=="paper" and p2[k2]=="scissor"):
    print("Player 2 wins,")
elif(p1[k1]=="scissor" and p2[k2]=="paper"):
    print("Player 1 wins,")
else:
    print("Player 2 wins,")
