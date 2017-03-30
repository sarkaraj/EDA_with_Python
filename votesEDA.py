import sys

import dataExtractor

dataFile = sys.argv[1]
saveFile = sys.argv[2]

df = dataExtractor.getDataFrameFromXml(dataFile)

# temp_df = df.sample(frac=0.01)
#
# print temp_df.describe

# print df
# print df.describe(include='all')

df.to_csv(saveFile, sep=',', header=True, index=True, line_terminator='\n')
