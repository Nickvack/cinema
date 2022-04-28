"""
This class is designed to create and send the ticket after the purchase.
It will have 2 methods, one to generate the ticket as a pdf file and one
to send it.
"""
import sqlite3
from fpdf import FPDF
import yagmail
import datetime
import time


class Tickets:
    connection = sqlite3.connect("cinema.db")
    cursor = connection.cursor()

    def generate_pdf(self, current_user, current_seat):
        self.movie_name = "Barbie 2, the return of the flying zombie monkeys!"
        generated_pdf = FPDF(orientation="P", unit="pt", format="A4")
        generated_pdf.add_page()

        generated_pdf.set_font(family="Times", size=24, style="B")
        generated_pdf.cell(w=0, h=80, txt=f"{self.movie_name}",
                           border=1, align="C", ln=1)
        generated_pdf.cell(w=0, h=80, txt="4:20PM - 08/09/2022", align="C", ln=1)
        generated_pdf.ln(h=40)
        generated_pdf.image("images/QR.png", w=300, h=300, x=150)

        generated_pdf.set_font(size=15, family="Helvetica")
        generated_pdf.cell(w=0, h=40, txt='Scan this QR to get more information about the '
                                          'movie.', ln=1, align="C")
        generated_pdf.cell(w=0, h=40, txt=f"User: {current_user[0][0]}", align="C", ln=1)
        generated_pdf.cell(w=300, h=40, txt=f"\tSeat number: {current_seat[0][0]}", align="C")
        generated_pdf.cell(w=200, h=40, txt=f"Ticket price: ${current_seat[0][2]}", align="C")
        generated_pdf.ln(h=40)
        generated_pdf.cell(w=0, h=40, align="C", ln=1,
                           txt=f"Please remember that bringing your own snacks"
                               f" is allowed and encouraged.")
        generated_pdf.ln(h=40)
        generated_pdf.image("images/popcorn.jpg", w=50, h=50, x=500)

        generated_pdf.output("Tickets/ticket.pdf")

    def send_email(self, current_user):
        email = yagmail.SMTP(user="nickvack1996@gmail.com", password="Azul_1023")
        email.send(to=f"{current_user[0][0]}",
                   subject=f"Ticket purchase for {self.movie_name} {datetime.datetime.now().date()}",
                   contents=f"Hey {current_user[0][0]}, here's your receipt for {self.movie_name}, "
                            f"please keep in mind that the movie starts at 4:20 and you need to"
                            f"bring your own snacks, we don't sell any snacks yet. \n"
                            f"Now, remember, always try your best and improve a little everyday! ",
                   attachments="Tickets/ticket.pdf")
        print(f"Please check your inbox at {current_user[0][0]}, we just sent you an "
              f"email with the ticket!")

