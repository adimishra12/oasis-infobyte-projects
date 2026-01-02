import datetime
import webbrowser


def greet():
    print("Hello! How can I help you today?")


def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"The current time is {current_time}")


def tell_date():
    today = datetime.date.today()
    print(f"Today's date is {today.strftime('%d %B %Y')}")


def search_web(query):
    print(f"Searching the web for '{query}' ...")
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(url)


def main():
    print("="*50)
    print("Simple Voice Assistant (text-based version)")
    print("="*50)
    print("Type 'hello', 'time', 'date', 'search <your query>', or 'exit' to quit.")
    print()

    while True:
        user = input("You: ").strip().lower()

        if user == "hello":
            greet()
        elif user == "time":
            tell_time()
        elif user == "date":
            tell_date()
        elif user.startswith("search "):
            query = user[len("search "):].strip()
            if query:
                search_web(query)
            else:
                print("Please enter something to search.")
        elif user == "exit":
            print("Goodbye!")
            break
        else:
            print("Sorry, I didn't understand that command.")


if __name__ == "__main__":
    main()
