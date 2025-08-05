with open("log.txt") as f:
    lines = f.readline()

lineno = 1
for line in lines:
    if("pyton" in line):
        print(f"pyton is present in line no:{lineno}")
        break
        lineno += 1

else:
        print("pyton is not present")