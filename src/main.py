name = input("Enter your name: ")

while True:
    # Displaying mood options
    print("Hii,", name, "\nHow are you feeling today?")
    print("1. Happy / Energetic")
    print("2. Sad / Low")
    print("3. Stressed / Anxious")
    print("4. Bored")

    attempts = 0

    # Loop for input validation (max 3 attempts)
    while True:
        if attempts >= 3:
            print("\nToo many invalid attempts. Exiting program.")
            exit()

        user_input = input("Enter your choice (1-4): ")

        # Checking if input is a number
        if user_input.isdigit():
            choice = int(user_input)

            # Checking if number is in valid range
            if choice in [1, 2, 3, 4]:
                break
            else:
                print("Invalid choice, please try again.")
        else:
            print("Please enter a valid number.")

        attempts += 1


    print(f"\nHey {name}, here are your recommended activities:\n")

    # Suggesting activities based on mood
    if choice == 1:
        print("• Do workout or sports")
        print("• Start a new project")
        print("• Hang out with friends")

    elif choice == 2:
        print("• Listen to music")
        print("• Take 15-minute walk")
        print("• Call a trusted friends or family members")

    elif choice == 3:
        print("• Practice deep breathing")
        print("• Try meditation")
        print("• Take a break and relax")

    elif choice == 4:
        print("• Try a new hobby")
        print("• Solve puzzles or games")
        print("• Explore something new")


    print("\nTip: Your mood affects your productivity, so choose wisely.")

    # Feedback loop (validates yes/no input)
    while True:
        feedback = input("\nWas this suggestion helpful? (yes/no): ").lower()

        if feedback == "yes":
            print("Great! I'm glad it works for you")
            break
        elif feedback == "no":
            print("Thanks for your feedback, we will improve!")
            break
        else:
            print("Invalid input, please enter 'yes' or 'no'.")

    # Asking user if they want to continue
    while True:
        again = input("\nDo you want to check another mood? (yes/no): ").lower()

        if again == "yes":
            break
        elif again == "no":
            print("\nThank you for using the system!")
            exit()
        else:
            print("Invalid input, please enter 'yes' or 'no'.")
