#spam 
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "click this"
message = input("Enter your message: ")
if ((p1 in message) or (p2 in message) or (p3 in message)):
    print("This comment us spam")
else:
    print("This comment is not spam")