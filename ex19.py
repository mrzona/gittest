def cheese_and_crackers(cheese_count, boxes_of_crackers):
     print(f"You have {cheese_count} cheeses")
     print(f"you have {boxes_of_crackers} boxes of crackers")
     print("Thats enough for a party")
     print("Get a blanket,\n")

print("We can give the function the numbers directly")
cheese_and_crackers(20,30)

print("OR, we can use variables from our script")
amount_of_cheese = 10 
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too")
cheese_and_crackers(10 + 20, 5 + 6)

print ("And we can combine the two variables and math")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def bilar(bilar_agda, bilar_salt):
    print(f"Jag har haft {bilar_agda} bilar")
    print(f"Jag har salt {bilar_salt} bilar")


bilar(23, 77)

egentligen_bilar_agda = 10
egentligen_bilar_salt = 10

bilar(egentligen_bilar_agda, egentligen_bilar_salt)