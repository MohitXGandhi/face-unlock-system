import os
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    while True:
        clear()
        print("=" * 40)
        print("   🔐 Real-Time Face Unlock System")
        print("=" * 40)
        print("  1. Register a New Face")
        print("  2. Launch Face Unlock")
        print("  3. List Registered Users")
        print("  4. Delete a User")
        print("  5. Exit")
        print("=" * 40)
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            from register_face import register_face
            register_face()
            input("\nPress Enter to go back to menu...")

        elif choice == "2":
            from unlock import unlock
            unlock()
            input("\nPress Enter to go back to menu...")

        elif choice == "3":
            list_users()
            input("\nPress Enter to go back to menu...")

        elif choice == "4":
            delete_user()
            input("\nPress Enter to go back to menu...")

        elif choice == "5":
            print("\n👋 Goodbye!\n")
            sys.exit()

        else:
            print("❌ Invalid choice. Please try again.")
            input("Press Enter to continue...")

def list_users():
    import pickle
    ENCODINGS_PATH = "models/faces.pkl"
    if not os.path.exists(ENCODINGS_PATH):
        print("\n❌ No registered users found.")
        return
    with open(ENCODINGS_PATH, "rb") as f:
        data = pickle.load(f)
    names = data["names"]
    if not names:
        print("\n❌ No registered users found.")
        return
    print("\n👥 Registered Users:")
    print("-" * 20)
    for i, name in enumerate(names, 1):
        print(f"  {i}. {name}")
    print(f"\nTotal: {len(names)} user(s)")

def delete_user():
    import pickle
    ENCODINGS_PATH = "models/faces.pkl"
    if not os.path.exists(ENCODINGS_PATH):
        print("\n❌ No registered users found.")
        return
    with open(ENCODINGS_PATH, "rb") as f:
        data = pickle.load(f)
    names = data["names"]
    if not names:
        print("\n❌ No registered users found.")
        return
    print("\n👥 Registered Users:")
    for i, name in enumerate(names, 1):
        print(f"  {i}. {name}")
    try:
        choice = int(input("\nEnter number to delete: ").strip())
        if 1 <= choice <= len(names):
            removed = names[choice - 1]
            data["names"].pop(choice - 1)
            data["encodings"].pop(choice - 1)
            with open(ENCODINGS_PATH, "wb") as f:
                pickle.dump(data, f)
            print(f"✅ '{removed}' deleted successfully!")
        else:
            print("❌ Invalid choice.")
    except ValueError:
        print("❌ Please enter a valid number.")

if __name__ == "__main__":
    menu()