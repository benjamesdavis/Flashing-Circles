import csv
import random

def status():
    if random.randint(0,1) == 1:
        return 'occupied'
    else:
        return 'empty'

def main():
    with open ('data-files/data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['status'])
        for n in range(1,10):
            writer.writerow([status()])

if __name__ == "__main__":
    main()
