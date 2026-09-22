import random
subjects = [
    "Akshay Kumar",
    "Modi ji",
    "A suspicious monkey",
    "Auto wale bhaiya",
    "Your neighbour's cat",
    "A Delhi metro passenger",
    "Sharma ji ka beta",
    "A very unemployed pigeon",
    "Your ex",
    "An overconfident mosquito"
]

action = [
    "declares war on",
    "gets caught dancing with",
    "becomes the CEO of",
    "starts a podcast about",
    "runs away after seeing",
    "gets emotionally attached to",
    "accidentally marries",
    "files a complaint against",
    "challenges to a WWE match",
    "says 'trust me bro' and buys"
]

place_or_thing = [
    "a plate of momos",
    "India Gate",
    "the Delhi Metro",
    "a random pani puri wala",
    "an unpaid electricity bill",
    "a ₹10 packet of Kurkure",
    "the last brain cell",
    "a Wi-Fi router",
    "an innocent samosa",
    "the entire population of Noida"
]
while True:
    print(random.choice(subjects))
    print(random.choice(action))
    print(random.choice(place_or_thing))
    headline = f"{random.choice(subjects)} {random.choice(action)} {random.choice(place_or_thing)}"  
    print(f"\n{headline}")
    user_input = input("\n🎭 Plot twist! Want another headline? (yes/no): ")
    if user_input=="no":
        break
#print goodbye message
print("\n📰 Thanks for using the Fake News Generator! Remember: if it sounds too crazy to be true... it probably belongs here. 😂")