def main():
    again = True
    while (again):
        try:
            print("Password Book\n_____________")
            title = input("What is the website name: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")

            password_book = open("Password Book.txt", "a")
            password_book.write("____\nName: " + title + "\nUsername: " + username + "\nPassword: " + password + "\n____")
            password_book.close()
        except Exception:
            print("An error has happened")
        do_again = input("Do you want to save another password and username: (y/n) ")
        if do_again != "y":
            again = False
            # password_book.close()
main()
