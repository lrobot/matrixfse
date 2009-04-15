import pysvg as g
fout=open('out.svg','wb')

root=g.parse('TMs10kSVGDemo.svg')
root.export(fout, 0, namespace_='',namespacedef_='xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"', name_='')
fout.close()