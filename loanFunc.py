from matplotlib import pyplot

def get_loan_info():
  """Get the basic information of a loan and store it in a dictionary"""
  #Create a blank dict to represent a loan
  loan = {}
 
  #Get user input for the categories of the loan
  loan['principal'] = float(input("Enter the loan amount: "))
  loan['rate'] = float(input("Enter the interest rate: "))/100
  loan['monthly payment'] = float(input("Enter the desired monthly payment amount: "))
  loan['money paid'] = 0
 
  return loan
 
 
def show_loan_info(loan, number):
  """Display the current loan status"""
  print("\n----Loan information after " + str(number) + " months----")
  for key, value in loan.items():
    print(key.title() + ": " + str(value))
 
 
def collect_interest(loan):
  """Update loan for interest per month"""
  #Divide by 12 to simulate collecting interest monthly
  loan['principal'] = loan['principal'] + loan['principal']*loan['rate']/12

def make_monthly_payment(loan):
  """Simulate making a monthly payment to pay down the principal"""
  loan['principal'] = loan['principal'] - loan['monthly payment']
 
  #You are required to make a full payment this month, you have not yet payed off your loan
  if loan['principal'] > 0:
    loan['money paid'] += loan['monthly payment']
  #You are not required to make a full payment this month, you have payed off your loan
  else:
 #For this else block, loan['principal'] will be negative
    loan['money paid'] += loan['monthly payment'] + loan['principal']
    loan['principal'] = 0


def summarize_loan(loan, number, initial_principal):
  """Display the results of paying off the loan"""
  print("\nCongraulations! You paid off your loan in " + str(number) + "months!")
  print("Your initial loan was $" + str(initial_principal) + " at a rate of "+ str(100*loan['rate']) + "%.")
  print("Your monthly payment was $" + str(loan['monthly payment']) + ".")
  print("You spent $" + str(round(loan['money paid'], 2)) + " in total.")

  #Calculate money spent on interest
  interest = round(loan['money paid'] - initial_principal, 2)
  print("You spent $" + str(interest) + " on interest!")

def create_graph(data, loan):
  """Create a graph to show the relationship between principal and time"""
  x_values = [] #These represent month numbers
  y_values = [] #These represent corresponding principal values
 
  #Loop through data set. Point is a tuple.
  #point[0] represents a month number, point[1] represents a principal value.
  for point in data:
    x_values.append(point[0])
    y_values.append(point[1])
 
  #Create a plot for x_values and y_values (month number and principal)
  pyplot.plot(x_values, y_values)
  pyplot.title(str(100*loan['rate']) + "% Interest With $" + str(loan['monthly payment']) + " Monthly Payment")
  pyplot.xlabel("Month Number")
  pyplot.ylabel("Principal of Loan")
 
  #Display the created graph
  pyplot.show()
