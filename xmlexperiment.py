import xml.etree.ElementTree as ET

tree = ET.parse('movies.xml')


root = tree.getroot()

#print(ET.tostring(root, encoding='utf8').decode('utf8'))

root.tag
for movie in root.findall("./genre/decade/movie/[year='1985']"):
  print(movie.attrib)

for movie in root.iter('movie'):
    print(movie.attrib)

b2tf = root.find("./genre/decade/movie[@title='Back 2 the Future']")
b2tf.attrib["title"] = "Gerwin"
#print(b2tf.attrib)

tree.write("movies.xml")


testje = tree.find("Gerwin")
print(testje)
