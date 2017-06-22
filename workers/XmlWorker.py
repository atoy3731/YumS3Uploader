
from lxml import etree as ET
import re
import gzip
from contextlib import closing

def __get_root__(file):
    if file.endswith('.gz'):
        with gzip.open(file) as archive:
            content = archive.read()
    else:
        with open(file) as archive:
            content = archive.read()

    return ET.fromstring(content)


def parse_repomd_xml(file):
    root = __get_root__(file)

    for d in root.getchildren():
        if 'type' in d.attrib:
            if d.attrib['type'] == 'filelists':
                for c in d.getchildren():
                    ntag = __normalize_tag__(c.tag)
                    if ntag == 'location':
                        print c.attrib['href'].split('/')[1]

def __normalize_tag__(tag):
    return re.sub(r'{.+}', '', tag)

