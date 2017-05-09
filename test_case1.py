#coding=utf-8
from xml.dom import minidom


#打开xml文档
dom = minidom.parse("info.xml")

#得到文档元素对象
root = dom.documentElement
print root.nodeName
print root.nodeValue
print root.nodeType
print root.ELEMENT_NODE
print

root = dom.documentElement

bb = root.getElementsByTagName('maxid')
b= bb[0]
print b.nodeName

bb = root.getElementsByTagName('login')
b= bb[0]
print b.nodeName