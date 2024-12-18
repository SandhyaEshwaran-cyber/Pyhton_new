a1={id:101,"name":"python","loc":"BLR"}
print(type(a1))
print(a1)
a1[id]=102
print(a1)
a1["sal"]=5400000
print(a1)
print(a1["loc"])


b1={
    101:"Java",
    102:"Python",
    103:{
        "Python":"Pandas",
        "Java":"Sprint"
        }
    }
print(b1)
print(b1[103]["Python"])