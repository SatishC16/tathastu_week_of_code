r1 = int(input("Enter runs scored by player1 : "))
r2 = int(input("Enter runs scored by player2 : "))
r3 = int(input("Enter runs scored by player3 : "))

print("Strike rate of Player 1 :",(r1*100/60))
print("Strike rate of Player 2 :",(r2*100/60))
print("Strike rate of Player 3 :",(r3*100/60))

print("Runs scored if Player1 played 60 more balls:",r1*2)
print("Runs scored if Player2 played 60 more balls:",r2*2)
print("Runs scored if Player3 played 60 more balls:",r3*2)

print("Maximum number of sixes Player1 could have hit:",r1//6)
print("Maximum number of sixes Player2 could have hit:",r2//6)
print("Maximum number of sixes Player3 could have hit:",r3//6)
