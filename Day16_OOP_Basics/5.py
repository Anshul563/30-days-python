class Player:
    # The __init__ method is triggered automatically
    def __init__(self, username, level):
        self.username = username  # Creating an instance attribute
        self.level = level        # Creating an instance attribute

# Creating the object automatically runs __init__
player1 = Player("GamerFaker", 50)

print(player1.username)  # Output: GamerFaker
print(player1.level)     # Output: 50