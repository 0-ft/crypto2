# stronger = adversary has more powers, weaker = adversary has less powers
def strong_to_weak_attack(stronger, weaker):
    print(f"To prove that a scheme secure against {stronger} is also secure against {weaker}, we can create a reduction from a {weaker} adversary to a {stronger} adversary.")
    print(f"Don't forget: reduction logic => reduction => complexity => advantage => (assumptions)")



# CPA attack is easier for the adversary than KPA attack. Easier to win CPA than KPA.
# CPA is a weaker guarantee than KPA. CPA is easier to achieve than KPA.
# So CPA-security is a *stronger* guarantee than KPA-security. They can't win even when we make it easy.

# def hard_to_easy_goal(harder, easier):
#     print(f"To prove that a {harder} secure scheme is also {easier} secure, we can create a reduction from an {easier} adversary to a {harder} adversary.")

# strong_to_weak_adversary("1cpa", "1kca")
# hard_to_easy_goal("1cpa", "1kca")

# EUF adversary has more powers because they get to choose the message
# UUF adversary has less powers because they don't get to choose the message
# EUF goal is easier to achieve than UUF goal
# UUF unforgeability is a weak security goal, because it's the hardest thing for an attacker to do
# strong_to_weak_attack("EUF", "UUF")
# strong_to_weak_attack("EUF", "UUF")
