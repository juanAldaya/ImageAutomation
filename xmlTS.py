try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree

    
def find_element_by_attribute(tree, attr_name, attr_value):
    """
    Finds an element by the specified attribute name and value in the given XML tree.

    Args:
        tree (etree.ElementTree): The XML tree to search.
        attr_name (str): The name of the attribute to search for.
        attr_value (str): The value of the attribute to search for.

    Returns:
        etree.Element or None: The found element or None if not found.
    """
    xpath_query = f"//*[@{attr_name}='{attr_value}']"
    found_elements = tree.xpath(xpath_query)
    return found_elements[0] if found_elements else None

def pretty_print_xml(xml_file):
    temp = etree.parse(xml_file)
    new_xml = etree.tostring(temp, pretty_print=True, encoding=str)
    print(new_xml)


def find_parent_element(tree, attr_name, attr_value):
    """
    Finds the parent element of an element with the specified attribute name and value.

    Args:
        tree (ElementTree): The XML tree.
        attr_name (str): The name of the attribute to search for.
        attr_value (str): The value of the attribute to search for.

    Returns:
        Element or None: The parent element or None if not found.
    """
    for element in tree.iter():
        if element.get(attr_name) == attr_value:
            return element.getparent()
    return None



def insert_element_into_xml(xml_path, parent_tag, new_element):
    """
    Inserts a new element into an existing XML file.

    Args:
        xml_path (str): Path to the existing XML file.
        parent_tag (str): Tag name of the parent element where the new element should be inserted.
        new_element (etree.Element): The new element to insert.
    """
    try:
        # Read the existing XML file
        tree = etree.parse(xml_path)

        # Find the parent element where the new element should be inserted
        parent_element = tree.find(f".//{parent_tag}")

        if parent_element:
            # Insert the new element
            parent_element.append(new_element)

            # Write the updated tree back to the file
            tree.write(xml_path, pretty_print=True, xml_declaration=True, encoding="utf-8")
            print(f"Element inserted into {xml_path}")
        else:
            print(f"Parent element '{parent_tag}' not found in the XML.")
    except Exception as e:
        print(f"Error: {e}")

def find_element_by_name_and_tag(root, tag_name, element_name):

    element = root.find('.//{0}[@name="{1}"]'.format(tag_name, element_name))
    return element

def insertElementInTree (xml_file, index, groupElement, toInsert):
    tree = etree.parse(xml_file)
    root = tree.getroot()
    parentInDest = find_element_by_name_and_tag(xml_file, groupElement.tag, groupElement.attrib['name'])
    parentInDest.insert(index, toInsert)


def searchElementIndexes (xmlRoot, listOfvalues): #in the list name is [0] y tag [1]  
    
    node = find_element_by_name_and_tag(xmlRoot, listOfvalues[1], listOfvalues[0])
    parentToIterate = node.getparent()
    i = 0
    for nodeInParent in parentToIterate:
        if nodeInParent.tag == node.tag:
            if nodeInParent.attrib['name'] == node.attrib['name']:
                listOfvalues.append(i)
                return listOfvalues
        i += 1

def addIndexInsertElements (listOfElementsToInsert, xmlRoot):
    i = 0

    for node in listOfElementsToInsert:
        node = searchElementIndexes(xmlRoot, node)
    
    return listOfElementsToInsert




def modifyTaskSequencePrep(pathToCopy, pathToModify):
    listTsPrep = [["Hardware Validate Custom", 'group'],["Copy OEM Files", 'step'], ["Replace APPWin Files", 'group'] , 
                  ['copy pharos files', 'step'], ['Install Dell Command Update','step'], ["Install Pharos",'step'], 
                  ["Install Lenovo System Update","step"],["Install Microsoft Office 365 32-Bit English","step"],
                  ["Set Balance Performance Power Scheme","step"], ["Disable Hibernation","step"],  ["Disable Standby", "step"],
                  ["Save APP Network Credentials", "step"],["OEM Custom Tasks", 'group'], ["Restart computer | Lenovo L14 series", "step"], 
                  ["Play MFA Sound", "step"], ["Launch APPWin", "group"]]


    treeTsMay = etree.parse(pathToModify)
    treeTsApr = etree.parse (pathToCopy)

    tsMay = treeTsMay.getroot()
    tsApr = treeTsApr.getroot()


    listTsPrep = addIndexInsertElements(listTsPrep, tsApr)
    
    for elements in listTsPrep:

        findedElement = find_element_by_name_and_tag(tsApr, elements[1], elements[0])

        findedParent = find_element_by_name_and_tag(tsMay, "group", findedElement.getparent().attrib['name'])

        findedParent.insert(int(elements[2]), findedElement)## inserta la modificacion (el nodo nuevo) al arbol nuevo

    etree.ElementTree(tsMay).write(pathToModify) ##ezcribe el tree modificado en el .xml original   


def modifyTaskSequenceProv(pathToCopy, pathToModify):
    
    treeTsProvMay = etree.parse(pathToModify)
    treeTsProvApr = etree.parse(pathToCopy)


    rootProvMay = treeTsProvMay.getroot()
    rootProvApr = treeTsProvApr.getroot()




    stepsListProv = [["Delete old Mapped drive", "step"], [ "NoSkip Shortcut for APP", "step"], ["LATAM BPO Applications", "group"], 
                     ['Disable Intel LPM', 'step'],['Allow Password Reset (SSPR)', 'step'],["Install Solstice", "step"],["Install Global Protect", "step"], ["Disable StandBy", "step"],
                     ["Disable Sleep and Hibernation", "step"],["GPUpdate after Admin Login", "step"], 
                     ["Set PostAction | Final GPUpdate", "step"], ["Forget Cached Credentials", "step"], 
                     ["Delete Direct Access LTS", "step"], ["Play Health Check sound alert", "step"]]

    stepsListProv = addIndexInsertElements(stepsListProv, rootProvApr)


    for elements in stepsListProv:

        findedElement = find_element_by_name_and_tag(rootProvApr, elements[1], elements[0])

        findedParent = find_element_by_name_and_tag(treeTsProvMay, "group", findedElement.getparent().attrib['name'])

        findedParent.insert(int(elements[2]), findedElement)

    etree.ElementTree(rootProvMay).write(pathToModify)
    return None

# tsProvApr = "tsProvApr.xml"
# tsProvMay = "tsProvMay.xml"

#modifyTaskSequenceProv(tsProvApr, tsProvMay)


