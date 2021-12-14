# You are given a valid XML document, and you have to print its score.
# The score is calculated by the sum of the score of each element.
# For any element, the score is equal to the number of attributes it has.

# TEST ONLY RUNS IN HACKERRANK

import xml.etree.ElementTree as ET
import sys


def get_attr_number(node):
    count=0
    for element in node.iter():
        if len(element.attrib) > 0:
            count += len(element.attrib)

    return count


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = ET.ElementTree(ET.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))





