def formatText(text):
    return f"**{text.strip().capitalize()}**"


myList = ["Elzero", "Web", "School"]


myFormated = map(formatText, myList)
# print(list(myFormated))

for name in myFormated:
    print(name)
