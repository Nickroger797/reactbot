import random

# Function for reaction game
def reaction_game():
    reactions = ["👍", "👎", "😂", "🔥", "😍"]
    return random.choice(reactions)

# Function for AI reactions
def ai_reaction(message):
    if "happy" in message:
        return "😊"
    elif "sad" in message:
        return "😢"
    elif "angry" in message:
        return "😠"
    else:
        return "😐"
