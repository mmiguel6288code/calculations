def car_loan(principal, apr, num_months):
  rate=apr/100.0/12
  if rate > 0:
    discount_factor=((1+rate)**num_months-1)/(rate*(1+rate)**num_months)
  else:
    discount_factor = num_months 
  monthly_payment=principal/discount_factor
  total_payments=monthly_payment*num_months
  print('''  
  Principal = $%0.0f
  APR = %0.1f%%
  Number of Months = %d
  Monthly Payment = $%0.2f
  Total Payments = $%0.0f
  Total Interest Paid = $%0.0f
  ''' %(principal,apr,num_months,monthly_payment,total_payments,total_payments-principal))

if __name__ == '__main__':
    while True:
     car_loan(*[eval(x) for x in input('Enter <principal>, <APR>, <months>: ').split(',')]) 
