def rem(l, word):
    return [item for item in l if word not in item]

l = ["pyton", "lulu", "nabin", "manoj", "suryakanti", "in"]
print(rem(l, "in"))