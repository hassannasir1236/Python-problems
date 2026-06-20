import random

data = [
    {
        "name": "Instagram",
        "description": "Social media platform",
        "country": "USA",
        "follower_count": 650
    },
    {
        "name": "Cristiano Ronaldo",
        "description": "Footballer",
        "country": "Portugal",
        "follower_count": 620
    },
    {
        "name": "Lionel Messi",
        "description": "Footballer",
        "country": "Argentina",
        "follower_count": 500
    },
    {
        "name": "Kylie Jenner",
        "description": "Media personality",
        "country": "USA",
        "follower_count": 400
    }
]

score = 0


# Get random profile
def get_profile():
    return random.choice(data)


# Compare follower counts
def check_answer(a_followers, b_followers, user_choice):
    if a_followers > b_followers:
        return user_choice == "A"
    else:
        return user_choice == "B"


while True:

    A = get_profile()
    B = get_profile()

    # avoid same profiles
    while A == B:
        B = get_profile()

    print("\n------------- A --------------")
    print(A["name"], A["description"], A["country"])
    print("Followers: ?")

    print("\n------------- B --------------")
    print(B["name"], B["description"], B["country"])
    print("Followers: ?")

    choice = input("\nWho has more followers? Type 'A' or 'B': ").upper()

    is_correct = check_answer(
        A["follower_count"],
        B["follower_count"],
        choice
    )

    if is_correct:
        score += 1
        print(f"✅ Correct! Score: {score}")
    else:
        print(f"❌ Wrong! Final Score: {score}")
        break