import csv

def to_csv(input):
    data = [input]
    with open('distances.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(data)
    writeFile.close()