import csv

def to_csv(input):
    with open('distances.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(input)
    writeFile.close()