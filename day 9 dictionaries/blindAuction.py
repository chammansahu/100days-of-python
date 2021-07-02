# import logo
from art import logo

bids={}
isFinished=False

def highestBidder(bids):
    highest=0
    for bidder in bids:
        if bids[bidder] > highest:
            highest=bids[bidder]
            winner = bidder
    print(f"{winner} is highet bidder")        

print(logo)
while not isFinished:
    name=input("Ente your name")
    bid=int(input("Ente your bid amount"))
    bids[name]=bid
    isDone=input("are ther any one to bid,yes or no")
    if isDone=="yes":
         isFinished=True
         highestBidder(bids)
    elif isDone=="no" :
         print('enter another')
    else:
        print("try again")         
