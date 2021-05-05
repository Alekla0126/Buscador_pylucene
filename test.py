import json
import Tkinter

# --------------------------------> Se abre el archivo JSON.
f = open('files.json')
# -------------------------------->   Se regresa un JSON.
documents = json.load(f)

for index in range(len(documents['documents'][0])):
    print(index)
    name = "document"+str(index+1)
    print(documents['documents'][0][name]["title"])