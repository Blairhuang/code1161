sandwich_orders=['a','b','c','b','d','b']
finished_sandwich=[]

while 'b' in  sandwich_orders:
    sandwich_orders.remove('b')
for i in sandwich_orders:
    finished_sandwich.append(i)
    print('I made your '+i+' sandwich.')


 return "You got it!"




