import csv
fout=open("fulldataset.csv","a")
# first file:
for line in open("items_appart_2.csv"):
    fout.write(line)
# now the rest:    
for num in range(3,24):
    f = open("items_appart_"+str(num)+".csv")
    
    #f.next() # skip the header
    for line in f:
         fout.write(line)
    f.close() # not really needed
fout.close()
