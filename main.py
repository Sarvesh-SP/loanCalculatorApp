from loanFunc import *



print("Welcome to the Loan Calculator App\n")

  #Initialize variables
month_number = 0
my_loan = get_loan_info()
starting_principal = my_loan['principal']
data_to_plot = []

#Display starting conditions of loan
show_loan_info(my_loan, month_number)
input("Press 'Enter' to begin paying off your loan.")

  #Simulate paying off the loan as long as the loan's principal > 0
while my_loan['principal'] > 0:
  #You cannot get ahead of the interest, you will never pay off the loan so
  if my_loan['principal'] > starting_principal:
    break

  #It is possible to pay off the loan, so simulate a single month
  #Increment month number, collect interest, make a payment, add data to plot,
  month_number += 1
  collect_interest(my_loan)
  make_monthly_payment(my_loan)
  data_to_plot.append((month_number, my_loan['principal']))
  show_loan_info(my_loan, month_number)

  #The loan is either paid off in full or it can NEVER be paid off...
  #The loan was paid off in full
  if my_loan['principal'] <= 0:
    summarize_loan(my_loan, month_number, starting_principal)
    create_graph(data_to_plot, my_loan)
  #The loan can NEVER be paid off, can't get ahead of interest
  else:
    print("\nYou will NEVER pay off your loan!!!")
    print("You cannot get ahead of the interest! :-(")