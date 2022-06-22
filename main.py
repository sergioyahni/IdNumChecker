import pandas as pd
from idCheck.checker import id_checker

df = pd.read_excel("data/tour_guides_data.xlsx")
dff = df.copy()
newColumns = ["A", "B", "C", "D", "E"]
dff.columns = newColumns

idList = dff["A"].tolist()
listToCheck = list()
newNum = str()
isOk = list()

for number in idList:
    if len(str(number)) < 9:
        addendum = "0" * (9-len(str(number)))
        newNum = addendum + str(number)
    else:
        newNum = str(number)
    listToCheck.append(newNum)

for idNumber in listToCheck:
    if id_checker(idNumber):
        isOk.append("מספר ת.ז. תקין")
    else:
        isOk.append("מספר ת.ז. לא תקין")

df["תקינות ת.ז."] = isOk
df["מספר זהות"] = listToCheck
df = df.drop(columns="מספר תעודת זהות")

df.to_excel("report/id_checked.xlsx", index = False)