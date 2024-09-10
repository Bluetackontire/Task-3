import random

while True:
  name1 = input("What is P1's name: ").strip()
  name2 = input("What is P2's name: ").strip()

  if name1 != "" and name2 != "":
    print()
    break
  else:
    print("Please enter names for both")
    print()

card_colour = ["red", "black", "yellow"]
p1_cards = []
p2_cards = []

p1_choice2 = random.choice(card_colour) + str(random.randrange(1, 11))
l12 = p1_choice2
p2_choice2 = random.choice(card_colour) + str(random.randrange(1, 11))
l22 = p2_choice2

r = []
for d in card_colour:
  for g in range(1, 11):
    x = d + str(g)
    r.append(x)

#red beats black
#yellow beats red
#black beats yellow

for i in range(15):
  p1_choice2 = random.choice(r)
  l12 = p1_choice2
  r.remove(l12)
  p2_choice2 = random.choice(r)
  l22 = p2_choice2
  r.remove(l22)

  print(name1, "pulled", l12)
  print(name2, "pulled",l22)
  
  if "red" in l12 and "black" in l22:
    print(name1, "wins")
    p1_cards.append(p1_choice2)
    p1_cards.append(p2_choice2)
  elif "red" in l22 and "black" in l12:
    print(name2, "wins")
    p2_cards.append(p1_choice2)
    p2_cards.append(p2_choice2)
    
  elif "yellow" in l12 and "red" in l22:
    print(name1, "wins")
    p1_cards.append(p1_choice2)
    p1_cards.append(p2_choice2)
  elif "yellow" in l22 and "red" in l12:
    print(name2, "wins")
    p2_cards.append(p1_choice2)
    p2_cards.append(p2_choice2)
    
  elif "black" in l12 and "yellow" in l22:
    print(name1, "wins")
    p1_cards.append(p1_choice2)
    p1_cards.append(p2_choice2)
  elif "black" in l22 and "yellow" in l12:
    print(name2, "wins")
    p2_cards.append(p1_choice2)
    p2_cards.append(p2_choice2)
  elif "red" or "black" or "yellow" in l12 and l22:
    a_string = l12        #try and check wheather no. l12 or l22 is larger
    b_string = l22
    
    numbers = []
    for word in a_string:
       if word.isdigit():
          numbers.append(int(word))
         
    for word in b_string:
       if word.isdigit():
          numbers.append(int(word))
         
    # print(numbers)

    if numbers[0] > numbers[1]:
      print(name1, "wins")
      p1_cards.append(p1_choice2)
      p1_cards.append(p2_choice2)
    else:
      print(name2, "wins")
      p2_cards.append(p1_choice2)
      p2_cards.append(p2_choice2)

  print()

# p1_cards.sort()
# p2_cards.sort()
# print()
# print(p1_cards)
# print()
# print(p2_cards)
# print()

print(name1, "has", len(p1_cards), "cards in total")
print(name2, "has", len(p2_cards), "cards in total")
print()

if len(p1_cards) > len(p2_cards):
  print(name1, "wins overall")
  print(name1, "had", p1_cards)
  o = open("save.txt", "a")
  o.write(name1 + " : " + str(len(p1_cards)) + "\n")
  o.close()
elif len(p1_cards) < len(p2_cards):
  print(name2, "wins overall")
  o = open("save.txt", "a")
  o.write(name2 + " : " + str(len(p2_cards)) + "\n")
  o.close()
  print(name2, "had", p2_cards)
elif len(p1_cards) == len(p2_cards):
  print("It's a tie\nPlay again to decide a winner")

print()

score_file = "save.txt"
score = []
with open(score_file) as f:
    for line in f:
        score.append(line.strip())
score.sort(key=lambda x: int(x.split(" : ")[-1]),reverse = True)
print(score[:5])