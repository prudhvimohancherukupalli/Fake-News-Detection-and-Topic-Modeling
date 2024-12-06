import os
from dotenv import load_dotenv, find_dotenv
from utils import fake_news_detection, topic_modulation

# Load environment variables from .env file
dotenv_path = find_dotenv()
if dotenv_path == "":
    print("No .env file found. Ensure it's in the correct directory.")
else:
    print(f".env file found at: {dotenv_path}")
    load_dotenv(dotenv_path)

def main():
    print("Welcome to the Team Quantum Project")
    
    while True:
        print("\nPlease choose an option:")
        print("1. Fake News Detection")
        print("2. Topic Modulation")
        print("3. Quit")
        
        choice = input("Enter your choice (1/2/3): ")

        # Load API key
        API_KEY = os.getenv("HUGGINGFACE_API_KEY")
        
        if not API_KEY:
            print("API key not found. Please set the HUGGINGFACE_API_KEY environment variable.")
            return

        # Handle different choices
        if choice == "1":
            text = input("Enter the news article text to analyze: ")
            result = fake_news_detection(text, API_KEY)
            print("Fake News Detection Result:")
            print(f"Labels: {result['labels']}")
            print(f"Scores: {result['scores']}")
        
        elif choice == "2":
            text = input("Enter the text for topic modulation: ")
            result = topic_modulation(text, API_KEY)
            print("Topic Modulation Result:")
            print(result)
        
        elif choice == "3":
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
