a=["mango","orange","apple","mango","pappaya","watermelon","orange","grapes","apple","pappaya"]
b=[]
for x in a:
    if x not in b:
        b.append(x)
print(b)
