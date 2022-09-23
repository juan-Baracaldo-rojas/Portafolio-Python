#Beautiful Soup is a Python library for pulling data out of HTML and XML files,
from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
print('beautiful Soup Object')
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, 'html5lib')
print(soup.prettify())
print( 'tag')
tag_object=soup.title
print("tag object:",tag_object)
print("tag object type:",type(tag_object))
tag_object=soup.h3
print('Children, Parents, and Siblings')
print("tag object",tag_object)
tag_child =tag_object.b
print(tag_child)
parent_tag=tag_child.parent
print(parent_tag)
print(tag_object)
print(tag_object.parent)
sibling_1=tag_object.next_sibling
print(sibling_1)
sibling_2=sibling_1.next_sibling
print(sibling_2)
print(sibling_2.next_sibling)
print("HTML Attributes")
print(tag_child['id'])
print(tag_child.attrs)
#obtain the atribute to page HTMK
print(tag_child.get('id'))
##________ ___________________________________________
print('Navigable String')
tag_string=tag_child.string
print(tag_string)
print(type(tag_string))
unicode_string = str(tag_string)
print(unicode_string)
print("filter")
table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, 'html5lib')
table_rows=table_bs.find_all('tr')
table_rows
first_row =table_rows[0]
first_row
print(type(first_row))

first_row.td
for i,row in enumerate(table_rows):
    print("row",i,"is",row)
for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)

list_input=table_bs .find_all(name=["tr", "td"])
list_input
table_bs.find_all(id="flight")
list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
list_input
table_bs.find_all(href=True)
table_bs.find_all(href=False)
soup.find_all(id='boldest')
table_bs.find_all(string="Florida")
two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"
two_tables_bs= BeautifulSoup(two_tables, 'html.parser')
two_tables_bs.find("table")    
two_tables_bs.find("table",class_='pizza')
print("dowload and webscraping")
url="http://www.ibm.com"    
data  = requests.get(url).text 
soup = BeautifulSoup(data,"html5lib")  # create a soup object using the variable 'data'
for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>
    print(link.get('href'))
for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))
print("Scrape data from HTML tables")
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text
soup = BeautifulSoup(data,"html5lib")
#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>
#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))