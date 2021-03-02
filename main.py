your_pocket = []

the_sandwich = []

def make_sandwich():
    the_sandwich.append("bread")
    the_sandwich.append("cheese")
    the_sandwich.append("turkey")

make_sandwich()

def sandwich_giver():
   if "bread" and "cheese" and "turkey" in the_sandwich:
    nabbits_pocket.append("one_sandwich")

sandwich_giver()
print(your_pocket[0])
