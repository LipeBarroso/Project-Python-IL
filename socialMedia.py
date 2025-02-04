import xml.etree.ElementTree as ET

# Carregar o arquivo XML
tree = ET.parse("propertiestool.xml")  # nome do arquivo
root = tree.getroot()

# Percorrer os elementos do XML
for child in root:
    print(child.tag, child.attrib, child.text)

# Acessar elementos específicos
for elem in root.findall("tag_desejada"):
    print(elem.text)