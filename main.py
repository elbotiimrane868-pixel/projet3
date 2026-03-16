import os
import sys
from termcolor import colored

# Function to display the interactive menu

def display_menu():
    os.system('clear')  # Clear the console
    print(colored('AI Chatbot', 'cyan', 'on_grey', attrs=['bold']))
    print(colored('1. Start Chat', 'yellow'))
    print(colored('2. Exit', 'yellow'))
    
# Function to start the chatbot interaction

def start_chat():
    print(colored('You can start chatting with the AI. Type "exit" to quit.', 'green'))
    while True:
        user_input = input(colored('You: ', 'blue'))
        if user_input.lower() == 'exit':
            print(colored('Exiting chat. Goodbye!', 'red'))
            break
        process_input(user_input)

# Function to process user input (placeholder)

def process_input(user_input):
    # Here should be the logic to handle user input and return AI response
    print(colored('AI: This is a placeholder response.', 'magenta'))

# Main program entry point

def main():
    while True:
        display_menu()
        choice = input(colored('Choose an option: ', 'blue'))
        if choice == '1':
            start_chat()
        elif choice == '2':
            print(colored('Exiting program.', 'red'))
            sys.exit()
        else:
            print(colored('Invalid choice. Please select again.', 'red'))

if __name__ == '__main__':
    main()