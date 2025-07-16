# main.py

from ai.test_generator import generate_test_cases

if __name__ == "__main__":
    user_story = input("Paste a user story: ")
    tests = generate_test_cases(user_story)
    print("\nGenerated Test Cases:\n")
    print(tests)
