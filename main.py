#!/usr/bin/python3

# Import Libraries

from bs4 import BeautifulSoup
from requests import get
from re import compile, sub

# Download lasts seisms page and encode it in utf-8

r = get("http://sismologia.cl/links/ultimos_sismos.html")
r.encoding = 'utf-8'

# Save the whole page in html format 

latest = open("Latest.html", "w")
latest.write(r.text)
latest.close()

# Read the page

file = open("Latest.html", "r")
file = file.read()

# Creating the soup
soup = BeautifulSoup(file, "html.parser")

#Searching for all <tr> tags and erasing first column

table = soup.find_all("tr")
table = table[1::]


#Cleaning html function

def cleanhtml(raw_html):
    cleaner = compile('<.*?>')
    cleantext = sub(cleaner, ' ', raw_html)
    return cleantext

#spliting and cleaning the table

section = cleanhtml(str(table))
section = section.split(",")


#opening the report saving folder

save_results = open("inform.txt", 'w')
save_results.write("| Local Date and time  |  UTC Date and time |Latitude|Longitude|Depth[Km]|Magnitude|Agency|Geographical Reference \n")
save_results.write("______________________________________________________________________________________________________")
#Going through each element and parse each one

for element in section:
    
    element = element[2::]
    element = str(element)

    #Remove listing tags
    element = element.replace('[', '')
    element = element.replace(']', '')
    
    #print("Element: " + element)

    #split by any line jump
    slice = element.split("\n")    
    
   
    #Remove the word 'antartica' and save each line into the report file

    for piece in slice:
        piece = str(piece)

        if "rtica" in piece:
            continue
        else:
            #print("\n" + "Earthquake: " + piece)
            save_results.write("\n" + piece + "\n")

#close the report folder.

save_results.close()



test = open("inform.txt", 'r')

print(test.read())

test.close()

