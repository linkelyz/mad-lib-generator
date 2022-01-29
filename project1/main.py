#  goal is to have a template and ask the user to give inputs, 
#  then read out the final mad lib

template = ["A vacation is when you take a trip to some (adj1) place with your (adj2) family.", 
"Usually you go to some place that is near a/an (noun) or up on a/an (noun).",
"A good vacation place is one where you can ride (plural-noun) or play (game) or go hunting for (plural-noun).",
"I like to spend my time (ing) or (ing)."]

print("Welcome to Link's MadLib!")
print("Let's start:")

a = template[0].strip().split("(adj1)")
print(a[0] + "...")

print("Please type an adjective.")
response = str(input())


b = template[0].strip().replace("(adj1)", response).split("(adj2)")
print(b[0] + "...")
print ("Please type another adjective.")
response = str(input())
c = template[0].strip().replace("(adj1)", response).replace("(adj2)", response)
print(c)

