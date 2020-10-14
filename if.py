is_hot = False
is_cold = True

if is_hot:
    print('This is hot day')
    print('Take your umbrella')

elif is_cold:
    print('This is cold day')
    print('Take your jursy')
else:
    print('Normal day')
print('Every day is good, enjoy')

is_goodCredit = True
price = 1000000

if is_goodCredit:
    DownPayment = (price * 10 / 100)
    print(f'Downpayment = ${DownPayment}')
else:
    DownPayment = (price * 20 / 100)
    print(f'Downpayment = ${DownPayment}')
