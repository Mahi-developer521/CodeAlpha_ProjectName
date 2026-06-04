def chitti(msg):
    if(msg=="hello"):
        return "Hi!"
    elif(msg=="how are you"):
        return "I,m fine,thanks!"
    elif(msg=="bye"):
        return "Goodbye!"
    else:
        return 
while True:
    msg=input("YOU:").lower()
    response=chitti(msg)
    print("Bot:",response)
    if(msg=="bye"):
        break
    