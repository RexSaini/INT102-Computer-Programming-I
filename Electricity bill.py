name=str(input('Enter Customer Name='))
age=int(input('Enter Customer Age='))
address=str(input('Enter Customer Address='))
account=int(input('Enter Customer Account Numnber='))
meter_number=int(input('Enter Meter Number='))
c_m_r=int(input('Enter current meter reading value='))
p_m_r=int(input('Enter previous meter reading value='))
units_consumed=c_m_r - p_m_r
fixed_meter_rent=250

# calculate the customer electricity bill
if( c_m_r < p_m_r):
    print('Invalid Data Values')
    c_m_r=int(input('Enter correct current meter reading value='))
    p_m_r=int(input('Enter correct previous meter reading value='))
    units_consumed=c_m_r - p_m_r

if (units_consumed<=200):
    bill=units_consumed * 2
elif ( units_consumed >200 and units_consumed <=500):
    remaining=units_consumed -200
    bill=400+(remaining * 3)
elif ( units_consumed > 500 and units_consumed <=800):
    remaining=units_consumed -500
    bill=400+900+(remaining * 5)
elif ( units_consumed > 800 and units_consumed <=1000):
    remaining=units_consumed -800
    bill=400+900+1500+(remaining * 7)
else:
    remaining=units_consumed -1000
    bill=400+900+1500+1400+(remaining * 10)
gst=bill * 0.12
cgst=gst//2
sgst=gst//2
total_bill=bill+gst

# Bill Slip for customer
print('Name=',name)
print('Age=',age)
print('Address=',address)
print('Meter No=',meter_number)
print('Previous Meter Reading=',p_m_r)
print('Current Meter reading=',c_m_r)
print('Unit Consumed=',units_consumed)
print('Bill Generated on custmer account number=',account,' is=',bill)
print('12 GST amount=',gst)
print('SGTS amount 6 %=',sgst)
print('CGST amount 6 %=',cgst)
print('Custmer Has to pay the total bill including 12% GST=',total_bill)