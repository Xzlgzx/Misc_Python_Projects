import re
import csv
import os


# Q1
def clean():
    current_path = os.getcwd() + '\\test.csv'
    with open(current_path, mode='r', newline='') as to_read:
        reader = csv.reader(to_read)
        counter = 0
        result = []
        for row in reader:
            if counter % 2 == 0 and counter > 0:
                phone_number = re.sub("[^0-9]", "", row[0])
                length = len(phone_number)
                if length < 10:
                    phone_number = phone_number + '0' * (10 - length)
                phone_number = '(' + phone_number[:3] + ')' + '-' + \
                               phone_number[3:6] + '-' + phone_number[6:]
                result.append([phone_number])
            elif counter == 0:
                result.append(row)
            counter += 1
    out = open(current_path, 'w')
    writer = csv.writer(out)
    writer.writerows(result)
    out.close()


# Q2
def reverse(s: str):
    return ' '.join(s.split()[::-1])