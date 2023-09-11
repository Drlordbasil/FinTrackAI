import subprocess
I have made the following optimizations to the Python script:
- Used `subprocess.check_call()` instead of `subprocess.run()` to simplify the code.
- Removed the `try -except ` block and let the `subprocess.check_call()` handle exceptions.
- Used `elif ` instead of multiple `if ` statements.
- Removed unnecessary print statements.

Here's the optimized version of the script:

```python


def run_program():
    subprocess.check_call(["python", "main.py"])


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

I hope this optimized version of the script helps improve its performance and readability. Let me know if you have any further questions.
