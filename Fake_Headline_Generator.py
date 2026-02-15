import random
subjects = ["Mahatma Gandhi","Bengal Tiger","Dr. B.R. Ambedkar","A herd of Indian Elephant","Sachin Tendulkar","One-horned Rhinoceros","C.V. Raman","Asiatic Lion","Rabindranath Tagore","King Cobra","Sardar Vallabhbhai Patel","Snow Leopard","P.V. Sindhu","Sloth Bear","Amitabh Bachchan","Red Panda"]
actions = ["launches","cancles","damces with","eats","declares war on","orders","celebrates","riding a Buffalo"]
places_or_things = ["at Red Fort","Mumbai local train","a plate of samosa","inside the parliament","during IPL match","India Gate"]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    obj = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {obj}"
    print("\n" + headline)

    user_input = input("Do you want another headline (yes/no): ").strip()
    if user_input == "no":
        break

print("\nGoodbye!")