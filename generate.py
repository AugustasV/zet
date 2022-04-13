import os
import re
indexTextStart = """<!DOCTYPE html>
<html>
<head><title>Index of Zettelkasten</title></head>
<body>
    <h2>Index of Zettelkasten</h2>
    <hr>
    <ul>
        <li>
            <a href='../'>../</a>
        </li>
"""
indexTextEnd = """
    </ul>
</body>
</html>
"""

def index_folder(folderPath):
    print("Indexing: " + folderPath +'/')
    #Getting the content of the folder
    files = os.listdir(folderPath)
    #If Root folder, correcting folder name
    root = folderPath
    if folderPath == '.':
        root = 'Root'
    indexText = indexTextStart.format(folderPath=root)

    for file in files:
        #Avoiding index.html files and indexing only numbers
        if file != 'index.html' and re.sub(r'\D','',file):
            f = open(file + '/README.md', 'r')
            line = f.readline()
            indexText += "\t\t<li>\n\t\t\t<a href='" + file + "'>" + re.sub('#','',line) + "</a>\n\t\t</li>\n"
            f.close()
    #Create or override previous index.html
    index = open(folderPath+'/index.html', "w")
    #Save indexed content to file
    index.write(indexText)

#Indexing root directory (Script position)
index_folder('.')