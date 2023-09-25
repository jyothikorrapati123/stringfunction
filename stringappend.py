#string append
#operator overloading

fName = "Jyothi"
lname = "Sumathi"
print("fullname:"+fName+" "+lname)

#
fname = "1"
lname = "4"
print("fullname:"+fname+lname)

#fstring interpolation
fname = "Jyothi"
lname = "korrapati"
fullname = f" fullname:{fname} {lname}"
print(fullname)

# string join method
fname = "Jyothi"
lname = "Korrapati"
list = ("fullname:"+fname,lname)
print(' '.join(list))
#string split
email = "Jyothi@gmail.com"
print(email.split("@"))
#split lines
food: str = """
biryani,
noodles,
pizza,
burger.
"""
print(food.splitlines())
#partition lrom lef to right

email = "a@Jyothi@gmail.com"
print(email.partition("@"))
#
a = "biryani @ 7"
print(a.partition("@"))
a= "foodcoart$1"
print(a.partition("$"))
#r partition
a = "9fruits%8"
print(a.partition("%"))
