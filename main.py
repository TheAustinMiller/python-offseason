title = input("Please enter a song title: ")
list = []
for i in range(len(title)):
  list.append(title[i:i+1])
print("\nHere is your new song title:")
newTitle = ""
for i in range(len(list)):
  if list[i] == " ":
    list[i] = "."
  list[i] = list[i].lower()
  newTitle += list[i] + " "
print(newTitle)
