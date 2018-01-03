import csv
finput=open("fulldataset.csv","r")
fout = open("dataset_without_duplicate.csv","w")
alreadyadded = set()
for line in finput:
	if line not in alreadyadded:
		alreadyadded.add(line)
		fout.write(line)
finput.close()
fout.close()



# Way 2 using pandas
#import pandas as pd
#df = pd.read_csv("filewithdup.csv", sep=",")
#df.drop_duplicates(subset=None, inplace=True)
#df.to_csv("withoutduplicate.csv")


