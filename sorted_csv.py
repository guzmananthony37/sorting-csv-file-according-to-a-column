# Imports
import csv

# Constants
rank = 0
# opening our " data to be sorted " file
file = open('sample_data.csv','r')

# Reading as csv
csv_reader = csv.reader(file,delimiter=',')

# converting csv_object to list object
csv_list = list(csv_reader)

# opening new file where the sorted results are stored
file1 = open('sorted_sample_data.csv','w+')

# Inserting 1st row which contains names of columns along with rank ahead of the whole row
rows = csv_list[0]
file1.write("Rank,")
for i in rows:
    if i == rows[-1]:
        file1.write(i)
    else:
        file1.write(i + ',')
file1.write('\n')

# deducing 1st row and reverse sorting the csv_list
csv_list = csv_list[1:]
csv_list.sort(key= lambda x: x[-2], reverse=True)

# inserting each sorted row along with rank into sorted file
for i in csv_list:
    if rank == 0:
        prev_i = csv_list[csv_list.index(i)]    # previous data
        rank += 1
    else:
        prev_i = csv_list[csv_list.index(i) - 1] # previous data  used to check whether two persons got same marks or not
    if prev_i[-2] == i[-2]:           #if previous score is equal to current score rank wont change
        rank = rank
    else:
        rank += 1                     # else rank is incremented by 1
    file1.write(f'{rank},')           # writing rank to file
    for j in i:                       # writing remaining rows to file
        if j == i[-1] :
            file1.write(j)
        else:
            file1.write(j + ',')
    file1.write('\n')

# closing the opened files
file.close()
file1.close()


