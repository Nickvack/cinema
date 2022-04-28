from db_management.users import User
from db_management.movies import Movies
from tickets import Tickets

login = False

# This first while statement is to give the user the option to
# purchase multiple tickets
while True:
    # This second one is to get the user to sign in correctly, it needs
    # Work, but it should do the trick
    while not login:
        user = User()
        login = user.login()

    # This code returns the seat and movie information.
    movie = Movies()
    movie.verify_av()

    # This code is for the payment part of the code. Please refer to each class
    user.verify_payment()
    user.update_balance(float(movie.result[0][2]))
    movie.change_status()

    # This code is to generate the PDF file and send it to the user
    tickets = Tickets()
    tickets.generate_pdf(user.result, movie.result)
    tickets.send_email(user.result)

    # This last part is just to close the first while statement
    buy_more = input("You're all set! Would you like to buy another ticket? (y/n)")
    if buy_more == "n":
        break
