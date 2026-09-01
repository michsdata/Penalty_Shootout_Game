import random
import time

def play_penalty_shootout_v2():
    print(" Welcome to Terminal Penalty Shootout")
    print("Best of 5 rounds. Brace yourself for the drama...")
    print("-" * 48)
    
    zones = ["left", "center", "right"]
    player_score = 0
    computer_score = 0
    rounds = 5
    
    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")
        print(f"Score: Player {player_score} - {computer_score} Computer\n")
        
        # --- PLAYER'S TURN TO SHOOT ---
        player_shot = ""
        while player_shot not in zones:
            player_shot = input("You step up to the spot. Where will you aim? (left/center/right): ").lower().strip()
            
        computer_dive = random.choice(zones)
        
        print(f"\nYou strike the ball towards the {player_shot}...")
        time.sleep(1.5) 
        
        print(f"The keeper launches themselves to the {computer_dive}...")
        time.sleep(1.5) 
        
        if player_shot == computer_dive:
            print("❌ SAVED! The keeper got a strong hand to it!")
        else:
            print("⚽ GOAL! The net bulges!")
            player_score += 1
            
        time.sleep(1) 
            
        # --- COMPUTER'S TURN TO SHOOT ---
        print("\nNow you are in goal. The computer steps up...")
        player_dive = ""
        while player_dive not in zones:
            player_dive = input("Where will you dive? (left/center/right): ").lower().strip()
            
        computer_shot = random.choice(zones)
        
        print(f"\nThe computer strikes the ball towards the {computer_shot}...")
        time.sleep(1.5)
        
        print(f"You dive to the {player_dive}...")
        time.sleep(1.5)
        
        if computer_shot == player_dive:
            print("🧤 WHAT A SAVE! You guessed the right way!")
        else:
            print("⚽ GOAL! The computer finds the back of the net.")
            computer_score += 1
            
        time.sleep(2) 

    # --- FINAL RESULTS ---
    print("\n" + "=" * 48)
    print("=== FULL TIME ===")
    print(f"Final Score: Player {player_score} - {computer_score} Computer")
    
    if player_score > computer_score:
        print("🏆 Congratulations! You won the shootout!")
    elif player_score < computer_score:
        print("💔 Heartbreak! The computer wins this time.")
    else:
        print("🤝 It's a draw!")

if __name__ == "__main__":
    play_penalty_shootout_v2()