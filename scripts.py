days = int(input('How many days did you stay with the car? '))
km = float(input('How many KM have you walked? '))
pay = (days * 60) + (km * 0.15)
print('You need to pay USD {:.2f}'.format(pay))