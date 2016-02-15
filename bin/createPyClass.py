#!/usr/bin/env python2

""" Tool to create a new python class. """

import sys
import os
import string

pyFileTemplate = """\"\"\" $className$ \"\"\"


class $className$:

    def __init__(self):
        pass
"""

testFileTemplate = """#!/usr/bin/env python2

\"\"\" Unittest class $className$. \"\"\"

import $className$
import unittest


class $className$Test(unittest.TestCase):

    def test01(self):
        x = $className$.$className$()


if __name__ == '__main__':
    unittest.main()

"""

def main():

    if len(sys.argv) != 2:
        print("ussage: createPyClass.py <class_name>")
        sys.exit(1)

    className = sys.argv[1]
    pyFileName = className + ".py"
    testFileName = className + "Test.py"
    
    pyFileContents = pyFileTemplate.replace("$className$", className)
    testFileContents = testFileTemplate.replace("$className$", className)

    print(pyFileName, testFileName)

    pyFile = open(pyFileName, "w")
    testFile = open(testFileName, "w")
    
    pyFile.write(pyFileContents)
    testFile.write(testFileContents)
    
    pyFile.close()
    testFile.close()

    os.system("chmod a+x " + pyFileName)
    os.system("chmod a+x " + testFileName)

main()
