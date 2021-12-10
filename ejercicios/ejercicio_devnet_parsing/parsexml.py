# Fill in this file with the code from parsing XML exercise

import xml.etree.ElementTree as ET
import re

xml = ET.parse("myfile.xml")
root = xml.getroot()
print(root)
ns = re.match('{.*}', root.tag).group(0)
print(ns)

editconf = root.find("{}edit-config".format(ns))
print(editconf)

defop = editconf.find("{}default-operation".format(ns))
testop = editconf.find("{}test-option".format(ns))
# e. Add print statements to print the value of the <default-operation> and <test-option> elements.
print("The default-operation contains: {}".format(defop.text))
print("The test-option contains: {}".format(testop.text))