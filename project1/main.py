#  goal is to have a template and ask the user to give inputs, 
#  then read out the final mad lib

template = ["A vacation is when you take a trip to some (adj1) place with your (adj2) family.", 
"Usually you go to some place that is near a/an (noun1) or up on a/an (noun2).",
"A good vacation place is one where you can ride (plural-noun) or play (game) or go hunting for (plural-noun).",
"I like to spend my time (ing) or (ing)."]

print("Welcome to Link's MadLib!")
print("Let's start:")

def sent1():
    temp_first = template[0].strip().split("(adj1)")
    print(temp_first[0] + "...")
    global response1 
    response1 = input("Please type an adjective: ")
    response1 = response1.strip().lower().replace(" ", "")

    temp_second = template[0].strip().replace("(adj1)", response1).split("(adj2)")
    print(temp_second[0] + "...")
    global response2 
    response2 = input("Please type another adjective: ")
    response2 = response2.strip(" ").lower().replace(" ", "")
    temp_1_full = template[0].strip().replace("(adj1)", response1).replace("(adj2)", response2)
    print(temp_1_full)
sent1()

def sent2():
    temp_third = template[1].strip().split("(noun1)")
    print(temp_third[0] + "...")
    global response3 
    response3 = input("Please type a noun: ")
    response3 = response3.strip().lower().replace(" ", "")

    temp_fourth = template[1].strip().replace("(noun1)", response3).split("(noun2)")
    print(temp_fourth[0] + "...")
    global response4
    response4 = input("Please type another noun: ")
    response4 = response4.strip().lower().replace(" ", "")
    temp_1_full = template[0].strip().replace("(adj1)", response1).replace("(adj2)", response2)
    temp_2_full = template[1].strip().replace("(noun1)", response3).replace("(noun2)", response4)
    print(temp_1_full + " " + temp_2_full)
sent2()