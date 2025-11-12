name = input("What is your name? ")
print("Hello, " + name + "!")
# Ask the user for their age
age = input("How old are you? ")

# Ask for confirmation
confirmation = input("You entered " + age + ". Is that correct? (yes/no): ")

# Verify the response
if confirmation.lower().strip() == "yes":
    print("Great! Let's move on.")
else:
    print("Okay, let's try again.")
