import random

csv_writer = open('sample_data.csv', 'w')
csv_writer.write('Roll No,name,Score,\n')
for i in range(1, 101):
    csv_writer.write(f'rollno {i},A{i},{random.randint(0,200)},\n')
csv_writer.close()