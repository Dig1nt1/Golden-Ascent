import random

def play_fortune_towers():
    print("Welcome to Fortune Towers!")
    initial_bet = int(input("Enter your bet amount (100, 500, 1000): "))
    levels = 5
    multipliers = [1.5, 2.5, 4, 6, 10]
    current_level = 0
    winnings = initial_bet
    fortune_key = False  # One-time key to bypass failure
    golden_ladder_active = False
    
    # Randomly assign a level where the Fortune Key is awarded
    key_level = random.randint(1, levels)
    
    while current_level < levels:
        print(f"\nLevel {current_level + 1}: Choose a door (1, 2, or 3)")
        
        # Award the Fortune Key at the randomly selected level
        if current_level + 1 == key_level and not fortune_key:
            fortune_key = True
            print("🎁 Lucky! You found a Fortune Key! It will save you once from collapse.")
        
        # Activate Golden Ladder at Level 3
        if current_level == 2 and not golden_ladder_active:
            golden_ladder_active = True
            print("✨ Golden Ladder Activated! If you continue, your final winnings will get a 1.2x boost! But if you cash out now, you lose 20% of your winnings.")
        
        doors = ["Gold", "Silver", "Black"]
        random.shuffle(doors)  # Randomize door positions
        choice = int(input("Pick a door (1, 2, or 3): ")) - 1
        
        if doors[choice] == "Gold":
            winnings *= multipliers[current_level]
            print(f"🎉 Success! You move to the next level. Winnings: ₹{winnings:.2f}")
            current_level += 1
            
        elif doors[choice] == "Silver":
            print("⚪ Safe Zone! No win/loss. Choose again.")
            
        elif doors[choice] == "Black":
            if fortune_key:
                print("🔑 Fortune Key used! You bypass the Black Door.")
                fortune_key = False
                current_level += 1
            else:
                print("💀 Tower Collapsed! You lost your bet.")
                winnings = 0
                break
        
        if current_level > 0 and current_level < levels:
            decision = input("Do you want to cash out? (yes/no): ").lower()
            if decision == "yes":
                if golden_ladder_active:
                    winnings *= 0.8  # Apply 20% penalty
                    print(f"Golden Ladder penalty applied! You cashed out with ₹{winnings:.2f}!")
                else:
                    print(f"You cashed out with ₹{winnings:.2f}!")
                return
        
    if golden_ladder_active:
        winnings *= 1.2  # Apply Golden Ladder bonus
    print(f"Game Over! Your total winnings: ₹{winnings:.2f}")

# Start the game
if __name__ == "__main__":
    play_fortune_towers()
