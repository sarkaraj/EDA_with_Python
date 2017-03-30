import dataExtractor

dataFile = "./ai.stackexchange.com/Votes.xml"

df = dataExtractor.getDataFrameFromXml(dataFile)

# temp_df = df.sample(frac=0.01)
#
# print temp_df.describe

print df.describe(include='all')

