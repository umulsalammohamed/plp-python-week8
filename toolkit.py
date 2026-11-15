"""
Personal Mini-Toolkit Project
Brings together variables, inputs, conditionals, loops, and lists.
"""

import random

def show_todo_menu():
    """Tool 1: To-Do List Manager - Add, view, and remove tasks dynamically."""
    tasks = ["Learn Python basics", "Build final mini-toolkit project"]
    
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Back to Main Menu")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            print("\nYour Current Tasks:")
            if not tasks:
                print("  (Your task list is currently empty!)")
            else:
                for index, task in enumerate(tasks, start=1):
                    print(f"  {index}. {task}")
        elif choice == "2":
            new_task = input("Enter the task you want to add: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f" Success: '{new_task}' has been added.")
            else:
                print(" Task cannot be empty.")
        elif choice == "3":
            if not tasks:
                print(" Nothing to remove, your list is empty.")
                continue
            for index, task in enumerate(tasks, start=1):
                print(f"  {index}. {task}")
            try:
                rem_idx = int(input("Enter the number of the task to remove: "))
                if 1 <= rem_idx <= len(tasks):
                    removed = tasks.pop(rem_idx - 1)
                    print(f" Removed: '{removed}'")
                else:
                    print(" Invalid task number.")
            except ValueError:
                print(" Please enter a valid number.")
        elif choice == "4":
            print("Returning to Main Menu...")
            break
        else:
            print("❌ Invalid choice. Please enter a number between 1 and 4.")


def play_guessing_game():
    """Tool 2: Number Guessing Game - Guess a secret number with hints."""
    print("\n--- Number Guessing Game ---")
    print("I have picked a secret number between 1 and 20. Try to guess it!")
    
    secret_number = random.randint(1, 20)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess (1-20): "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"🎉 Congratulations! You found the secret number {secret_number} in {attempts} attempts!")
                break
        except ValueError:
            print("❌ Invalid input. Please enter a valid integer.")


def calculate_bill_split():
    """Tool 3: Tip & Bill Splitter - Calculate individual shares of a bill."""
    print("\n--- Tip & Bill Splitter Calculator ---")
    try:
        bill_amount = float(input("Enter the total bill amount ($): "))
        tip_percent = float(input("Enter tip percentage (e.g., 15, 18, 20): "))
        num_people = int(input("Enter number of people splitting the bill: "))
        
        if bill_amount < 0 or tip_percent < 0 or num_people <= 0:
            print("❌ Values must be greater than zero.")
            return
        
        total_tip = bill_amount * (tip_percent / 100)
        total_bill = bill_amount + total_tip
        per_person = total_bill / num_people
        
        print("\n--- Bill Summary ---")
        print(f"Subtotal:    ${bill_amount:.2f}")
        print(f"Tip ({tip_percent}%): ${total_tip:.2f}")
        print(f"Total Bill:  ${total_bill:.2f}")
        print(f"Each Person Pays: ${per_person:.2f}")
        print("--------------------")
    except ValueError:
        print("❌ Please enter valid numbers for money and people.")


def main():
    """Main program loop displaying the menu and routing choices."""
    print("========================================")
    print("       WELCOME TO YOUR MINI-TOOLKIT     ")
    print("========================================")
    
    while True:
        print("\nPlease choose a tool from the menu below:")
        print("  1. To-Do List Manager (Manage your tasks)")
        print("  2. Number Guessing Game (Test your luck)")
        print("  3. Tip & Bill Splitter (Calculate shares)")
        print("  4. Quit")
        print("========================================")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            show_todo_menu()
        elif choice == "2":
            play_guessing_game()
        elif choice == "3":
            calculate_bill_split()
        elif choice == "4":
            print("\nThank you for using Personal Mini-Toolkit. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()