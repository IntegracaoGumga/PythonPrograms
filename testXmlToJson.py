from xml.etree import ElementTree

tree = ElementTree.parse('/usr/pro/p/coopermota/dif/gumga/xmlProdutoGumga.xml')
print tree
root = tree.getroot()
product_elements = root.findall('produto')

for product_element in product_elements:
    print(ElementTree.tostring(product_element))
