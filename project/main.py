# main.py

from pet import Pet

# Create a pet object
name = input("🐶 What is your pet's name? ")
my_pet = Pet(name)

def show_menu():
    print("\n🔸 What would you like to do?")
    print("1. Feed")
    print("2. Sleep")
    print("3. Play")
    print("4. Teach a trick")
    print("5. Show learned tricks")
    print("6. Show status")
    print("7. Exit")

# Game loop
while True:
    show_menu()
    choice = input("Enter your choice (1–7): ")

    if choice == "1":
        my_pet.eat()
    elif choice == "2":
        my_pet.sleep()
    elif choice == "3":
        my_pet.play()
    elif choice == "4":
        trick = input("What trick do you want to teach? ")
        my_pet.train(trick)
    elif choice == "5":
        my_pet.show_tricks()
    elif choice == "6":
        my_pet.get_status()
    elif choice == "7":
        print(f"👋 Goodbye! {my_pet.name} will miss you!")
        break
    else:
        print("❌ Invalid choice. Please pick a number from 1 to 7.")
