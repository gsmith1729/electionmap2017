import pandas as pd
results=pd.ExcelFile(r"C:\Users\footb\Documents\politics stuff\2017geresults.xlsx")
presults=results.parse("UK 2015")
accres=presults.values
# list of constituency names
allcons=[accres[0][0]]
for i in range(1,len(accres)):
    if accres[i][0]!=accres[i-1][0]:
        allcons.append(accres[i][0])
#print(allcons)
# list of dictionaries of results
results=[]
res={"Conservative":26955}
for i in range(1,len(accres)):
    if accres[i][0]==accres[i-1][0]:
        res[accres[i][3]]=accres[i][4]
    else:
        res["name"]=accres[i-1][0]
        res["region"]=accres[i-1][1]
        results.append(res)
        res={}
        res[accres[i][3]]=accres[i][4]
res["name"]=accres[i-1][0]
res["region"]=accres[i-1][1]
results.append(res)
