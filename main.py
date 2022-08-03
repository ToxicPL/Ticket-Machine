print("Hello, this is software from Ticket Machine\n Please enter name of you ticket that you want to buy:")
print("****" * 16)
# Tables
tickets = {"normal", "weekly", "monthly"}

# Price
normal = 12
weekly = 25
monthly = 100

for z in (tickets):
    print(z)


ticket_number = input("| ")
ticket_number = ticket_number.lower()
if ticket_number in tickets:
    print(ticket_number)
else:
    quit()

