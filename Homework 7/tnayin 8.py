dictionary = {
    "Varible": "Փոփոխական", 
    "Declaration": "Հայտարարում",
    "Assignment": "Վերագրում",
    "Data tpyes": "Տվյալների տիպեր",
    "integer": "Թվային տիպ",
    "String": "Տողային տիպ",
    "Boolean": "Բուլյան տիպ",
    "true": "Ճշմարիտ",
    "else": "Հակառակ դեպքում",
    "array": "Զանգված",
    "if": "Եթե",
    "false": "Կեղծ"
}
n = input("input Word for translate:\t")
if n in dictionary:
    print(n,"-",dictionary[n])
else:
    print("the word is not in the dictionary")