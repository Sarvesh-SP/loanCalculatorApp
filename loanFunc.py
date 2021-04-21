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
    loan['monthly paid'] += loan['monthly payment']
  else:
    

def summarize():
  pass


def create_graph():
  pass
