import StringIO
from lxml import etree

def out_node(x):
    print etree.tostring(x)


fp = '/home/ubik/PycharmProjects/lenal/xpath_tests/examples/4.examples'

tree = etree.parse(open(fp))
x= tree.xpath('/project/title')


