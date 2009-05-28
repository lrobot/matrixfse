'''
Created on 26.05.2009

@author: kerim
'''

from pysvg import parser, core


def main():
    o = parser.parse('TMs10kSVGDemo.svg')
    f = open('./testoutput/out.svg', 'w')
    f.write(core.wrap_xml(o.getXML()))
    f.close()



if __name__ == "__main__":
    main()
