# You are given a valid XML document, and you have to print the maximum level of nesting in it. Take the depth of the root as
#
# Input Format
#
# The first line contains N, the number of lines in the XML document.
# The next N lines follow containing the XML document.
#
# Output Format
#
# Output a single line, the integer value of the maximum level of nesting in the XML document.

import xml.etree.ElementTree as ET

tree = ET.parse('sample.xml')
maxdepth = 0


def depth(element, level):  # counts how many depth levels does the xml have. Level 0 is root.
    global maxdepth

    if level == maxdepth:
        maxdepth += 1

    for child in element:
        depth(child, level + 1)


depth(tree.getroot(), -1)
print(maxdepth)
