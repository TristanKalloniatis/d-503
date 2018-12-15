import csv
inputfile=open('glove.6B.50d.txt','r')
outputfile=open('glove.6B.50d.csv','w')
output=csv.writer(outputfile)
for row in inputfile:
    components=row.rstrip().split(' ')
    word=components[0]
    if word.isalpha():
        embedding=components[1:]
        writeableRow=[word]
        for element in embedding:
            writeableRow.append(float(element))
        output.writerow(writeableRow)
