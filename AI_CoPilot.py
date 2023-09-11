import subprocess
```python


def run_program():
    subprocess.run(["python", "main.py"])


def chatbot():
    print("Welcome to the Expense Tracker Chatbot!")
    print("How can I assist you today?")

    while True:
        user_input = input("> ").lower()

        if user_input == "run program":
            print("Running the program...")
            run_program()
            print("Program execution completed.")
        elif user_input == "exit":
            print("Thank you for using the chatbot. Goodbye!")
            break
        else:
            print("Sorry, I didn't understand that. Please try again.")


if __name__ == "__main__":
    chatbot()
```

No further code optimizations were required as the code is already efficient and readable.
