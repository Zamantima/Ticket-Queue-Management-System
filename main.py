from queue import Queue

ticket = Queue()

def new_ticket(n):
    """"
    Add a new ticket tp teh queue
    """
    ticket.enqueue(n)
    print(f"Issued ticket number: {n}")

def serve_next():
    """"
    Serve teh next customer by displaying their ticket number
    """
    if ticket.queue_size() < 1:
        print("No customers in the queue")
    else:
        print(f"Serving ticket number: {ticket.peek()}")


def current_ticket():
    """"
    Displaying the current ticket being served adn remove it from the queue
    """
    if ticket.queue_size() < 1:
        print("No customers in the queue")
    else:
        print(f"Currently serving ticket {ticket.peek()}")
        ticket.dequeue()

def menu():
    """"
    Displaying the menu options
    """
    print("Menu:")
    print("1. Issue new ticket")
    print("2. Serve next customer")
    print("3. Display current ticket")
    print("4. Exit")
    print("\n")

def main():
    menu()
    user_choice = None
    n = 0
    while user_choice != 4:
        user_choice = int(input("Enter your choice: "))
        try:
            if user_choice == 1:
                n += 1
                new_ticket(n)
                print("\n")
            elif user_choice == 2:
                serve_next()
                print("\n")
            elif user_choice == 3:
                current_ticket()
            menu()
        except ValueError:
            print("Invalid input")
    print("Exiting program")

if __name__ == "__main__":
    main()