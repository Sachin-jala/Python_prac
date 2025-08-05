with open("log.txt") as f:
    content = f.read()

    if("pyton" in content):
        print("pyton is present")
    else:
        print("pyton is not present")