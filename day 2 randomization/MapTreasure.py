row1 = ["🎁", "🎁", "🎁"]
row2 = ["🎁", "🎁", "🎁"]
row3 = ["🎁", "🎁", "🎁"]
map = [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}\n")

position = input("where do you want to put treasure?");

row = int(position[0])
col = int(position[1])
map[row-1][col-1]='✡'
print(f"{row1}\n{row2}\n{row3}\n")
