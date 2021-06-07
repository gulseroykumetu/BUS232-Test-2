def calculateshares():

    shareholders = []
    share = int(input("Please enter the number of shares: "))
    shareholders.append(share)

    while share!=0:
        share = int(input("Please enter the number of shares: "))
        shareholders.append(share)


    shareholders.sort(reverse=True)

    sum = 0
    for i in shareholders:
        sum+=i
    
    needed = int(sum/2 + 1)

    support = 0
    supportcount = 0
    for i in shareholders:
        if support <= needed:
            support += i
            supportcount += 1
    
    print("Thank you, there is a total of {} shares represented here.".format(sum))
    print("Shared needed for majority vote is {}".format(needed))
    print("You need the support of top {} shareholders for this number of votes.".format(supportcount))

    f = open("results.txt", "w+")

    f.write("The shares are: \n")
    for i in range(len(shareholders)-1):
        f.write("{} \n".format(shareholders[i]))
    
    f.write("Thank you, there is a total of {} shares represented here. \n".format(sum))
    f.write("Shared needed for majority vote is {} \n".format(needed))
    f.write("You need the support of top {} shareholders for this number of votes. \n".format(supportcount))


calculateshares()