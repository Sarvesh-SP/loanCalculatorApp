from matplotlib import pyplot
def get_loan_info():
  loan = {}
  loan['principal'] = float(input('Enter the loan amount: '))
  loan['rate'] = float(input('Enter the interest rate: '))/100
  loan['monthly payment'] = float(input('Enter the desired monthly payment amount: '))
  loan['money paid'] = 0
  return loan


def show_info(loan, month):
  print(f'\n---Loan information after {month} months---')
  for key, value in loan.items():
    print(f'{key.title()} : {value}')


def collect_interest(loan):
  loan['principal'] = loan['principal'] + loan['principal']*loan['rate']/12

def make_monthly_payment(loan):
  loan['principal'] = loan['principal'] - loan['monthly payment']

  if loan['principal'] > 0:
    loan['money paid'] += loan['monthly payment']
  else:
    loan['money paid'] += loan['monthly payment'] + loan['principal']
    loan['principal'] = 0

def summarize(loan, num, initial_principal):
  print(f'\nCongratulations! You paid off your loan in {num}.')
  print(f'Your initial loan was ${initial_principal}  at a rate of {loan['rate']*100}%.')
  print(f'Your monthly payment was ${loan['monhtly payment'.]}')
  print(f'You spent ${round(loan['money paid'], 2)} in total.')

  #Calculate money spent on interest
  interest = round(loan['money paid'] - initial_principal, 2)
  print("You spent $" + str(interest) + " on interest!")

def create_graph(data, loan):
  """Create a graph to show the relationship between principal and time"""
  
  x_values = [] #These represent month numbers
  y_values = [] #These represent corresponding principal values

 #Loop through data set. Point is a tuple. #point[0] represents a month number, point[1] represents a principal value.
for point in data:
  x_values.append(point[0])
  y_values.append(point[1])

#Create a plot for x_values and y_values (month number and principal)
  pyplot.plot(x_values, y_values)
  pyplot.title(str(100*loan['rate']) + "% Interest With $" + str(loan['monthly
payment']) + " Monthly Payment")
  pyplot.xlabel("Month Number")
  pyplot.ylabel("Principal of Loan")

  #Display the created graph
  pyplot.show()
