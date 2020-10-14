has_high_income = True
has_good_credit = False

if has_good_credit or has_high_income:
    print('Eligibale for loan')

else:
    print('Not eligible')

#if a person has good credit and no criminal record, he has eligiable for loan

has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print('Eligible for loan')
else:
    print('Not eligible for loan')