#problem 24 check given usernamae contain 1p0 character or not
username = input("Enter username: ")
if (len(username) < 10):
    print("Username must contain 10 characters")
else:
    print("All is well")