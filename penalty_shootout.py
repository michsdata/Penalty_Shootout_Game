import random

def play_penalty_shootout():
    print(" Welcome to the Terminal Penalty Shootout ")
    print("Best of 5 rounds. Can you beat the keeper?")
    print("-" * 48)
    
    zones = ["left", "center", "right"]
    player_score = 0
    computer_score = 0
    rounds = 5
    
    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}")
        print(f"Score: Player {player_score} - {computer_score} Computer")
        
        # Player's turn to shoot
        player_shot = ""
        while player_shot not in zones:
            player_shot = input("Where will you shoot? (left/center/right): ").lower().strip()
            
        computer_dive = random.choice(zones)
        
        print(f"You aimed {player_shot}...")
        print(f"The keeper dived {computer_dive}!")
        
        if player_shot == computer_dive:
            print("❌ SAVED! The keeper read you perfectly.")
        else:
            print("⚽ GOAL! You buried it past the keeper.")
            player_score += 1
            
        # Computer's turn to shoot
        print("\nNow you are in goal. The computer is stepping up...")
        player_dive = ""
        while player_dive not in zones:
            player_dive = input("Where will you dive? (left/center/right): ").lower().strip()
            
        computer_shot = random.choice(zones)
        
        print(f"The computer aimed {computer_shot}...")
        print(f"You dived {player_dive}!")
        
        if computer_shot == player_dive:
            print("🧤 WHAT A SAVE! You denied the computer.")
        else:
            print("⚽ GOAL! The computer scores.")
            computer_score += 1

    print("\n" + "=" * 48)
    print("=== FINAL WHISTLE ===")
    print(f"Final Score: Player {player_score} - {computer_score} Computer")
    
    if player_score > computer_score:
        print("🏆 Congratulations! You won the shootout!")
    elif player_score < computer_score:
        print("💔 Heartbreak!Computer wins this time.")
    else:
        print("🤝 It's a draw! Sudden death awaits (next time).")

if __name__ == "__main__":
    play_penalty_shootout()
