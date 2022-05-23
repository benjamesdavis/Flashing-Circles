import csv
import random

def status():
    if random.randint(0,1) == 1:
        return 'occupied'
    else:
        return 'empty'

with open ('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['status'])
    for n in range(1,10):
        writer.writerow([status()])

print("hello")
