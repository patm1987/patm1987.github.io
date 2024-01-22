#!/usr/bin/env python3

import xml.etree.ElementTree as ET

if __name__ == '__main__':
    tree = ET.parse('blogger_export/feed.atom')
    root = tree.getroot()
    print('root: ', root.tag)
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        print("Entry: ", entry.tag, ' :: attrib:', entry.attrib)
        type = entry.find('{http://schemas.google.com/blogger/2018}type')
        if type is None:
            continue
        status = entry.find('{http://schemas.google.com/blogger/2018}status')
        if status is None:
            continue

        print('\tType', type.text)
        print('\tStatus', status.text)

        if type.text == 'POST' and status.text == 'LIVE':
            title = entry.find('{http://www.w3.org/2005/Atom}title').text
            published = entry.find('{http://www.w3.org/2005/Atom}published').text[:10]
            content = entry.find('{http://www.w3.org/2005/Atom}content').text
            generated_filename = f'{published}-{title.replace(" ", "")}.html'
            joined_content=f'<!-- title: {title} -->\n{content}'
            print('Title:', title)
            print('Published:', published)
            print('Generated Filename:', generated_filename)
            print('Content: ', content)
            print('\n')