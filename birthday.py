import datetime 

print("Welcome.")
m = input("Enter your birth month: >")
d = input("Enter your birth day: >")
y = int(input("Enter your birth year: >"))

print("You were born on:", m, d, y)

#Added stuff

TD = datetime.datetime.now()


print("You are ", str(TD.year - y), " Years old")
#Add a way to caculated age23
# Just adding this beacuse I forgot to put it in the origin

