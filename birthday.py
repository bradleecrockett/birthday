from datetime import date

print("Welcome.")
m = input("Enter your birth month: >")
d = input("Enter your birth day: >")
y = input("Enter your birth year: >")

print("You were born on:", m, d, y)

#Added stuff

TD = date.today()

print("You are ", TD.year() - y, "Years old")
#Add a way to caculated age
# Just adding this beacuse I forgot to put it in the origin

