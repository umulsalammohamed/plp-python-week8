import random

# ==========================================
# TOOL 1: To-Do List Manager
# ==========================================
def todo_manager():
    """Allows the user to view, add, and remove tasks from a dynamic list."""
    tasks = ["Buy groceries", "Complete Python project"]
    
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Back to Main Menu")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            if not tasks:
                print("\nYour to-do list is currently empty.")
            else:
                print("\nCurrent Tasks:")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
                    
        elif choice == '2':
            new_task = input("Enter the new task: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"'{new_task}' added successfully!")
            else:
                print("Task cannot be empty.")
                
        elif choice == '3':
            if not tasks:
                print("\nNo tasks to remove.")
            else:
                print("\nCurrent Tasks:")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
                try:
                    rem_index = int(input("Enter the number of the task to remove: "))
                    if 1 <= rem_index <= len(tasks):
                        removed = tasks.pop(rem_index - 1)
                        print(f"Removed '{removed}' from your list.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
                    
        elif choice == '4':
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please pick a number between 1 and 4.")


# ==========================================
# TOOL 2: Number Guessing Game
# ==========================================
def number_guessing_game():
    """A game where the user tries to guess a randomly generated secret number."""
    print("\n--- Number Guessing Game ---")
    print("I've picked a number between 1 and 50. Can you guess it?")
    secret_number = random.randint(1, 50)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess (or enter 0 to exit game): "))
            if guess == 0:
                print("Exiting game. Better luck next time!")
                break
            
            attempts += 1
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts!")
                break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


# ==========================================
# TOOL 3: Tip & Split Calculator
# ==========================================
def tip_calculator():
    """Calculates the tip amount, total bill, and split per person."""
    print("\n--- Tip & Split Calculator ---")
    try:
        bill = float(input("Enter the total bill amount ($): "))
        if bill < 0:
            print("Bill amount cannot be negative.")
            return
        
        tip_percent = int(input("Enter tip percentage (e.g., 10, 15, 20): "))
        people = int(input("Enter number of people splitting the bill: "))
        
        if people <= 0:
            print("Number of people must be at least 1.")
            return
        
        tip_amount = bill * (tip_percent / 100)
        total_bill = bill + tip_amount
        per_person = total_bill / people
        
        print(f"\n--- Bill Summary ---")
        print(f"Bill Subtotal: ${bill:.2f}")
        print(f"Tip ({tip_percent}%): ${tip_amount:.2f}")
        print(f"Total with Tip: ${total_bill:.2f}")
        print(f"Each person pays: ${per_person:.2f}")
    except ValueError:
        print("Please enter valid numeric values.")


# ==========================================
# MAIN PROGRAM MENU LOOP
# ==========================================
def main():
    print("==========================================")
    print("   Welcome to Your Personal Mini-Toolkit! ")
    print("==========================================")
    
    while True:
        print("\n==============================")
        print("      MAIN MENU")
        print("==============================")
        print("1. To-Do List Manager")
        print("2. Number Guessing Game")
        print("3. Tip & Split Calculator")
        print("4. Quit")
        print("------------------------------")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            todo_manager()
        elif choice == '2':
            number_guessing_game()
        elif choice == '3':
            tip_calculator()
        elif choice == '4':
            print("\nThank you for using Personal Mini-Toolkit. Goodbye! 👋")
            break
        else:
            print("\n⚠️ Invalid choice! Please select a valid menu option between 1 and 4.")

if __name__ == "__main__":
    main()