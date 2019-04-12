import pandas as pd
rd=pd.read_csv("HalfHourParentTeacherConferenceSampleImportFile.csv",index_col=1)
print(rd)

rd.drop(['Contact ','Event Title '], axis=1,inplace=True)

rd.to_csv("output_HalfHourParentTeacherConferenceSampleImportFile.csv")
