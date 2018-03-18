#!/usr/bin/env python3

""" Tool to create new cpp class. """

import sys
import os
import string
import re

def camelCaseSplit(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    return [m.group(0) for m in matches]

def camelCaseUpper(identifier):
    l = camelCaseSplit(identifier)
    l2 = [x.upper() for x in l]
    return "_".join(l2)

hFileTemplate = """#ifndef $CLASS_NAME$_H
#define $CLASS_NAME$_H

class $className$
{
public:
	$className$();
	~$className$();
};

#endif
"""

cppFileTemplate = """#include <$className$.h>

$className$::$className$() { }
$className$::~$className$() { }
"""

testFileTemplate = """#include <$className$.h>
#include <Usutf.h>

USUTF_TEST(test$className$)
{
	$className$ x;
	Usutf::test(true);
}
"""

def main():

    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("ussage: createClass.py [-t] <class_name>")
        sys.exit(1)

    generateTest = False
    for x in sys.argv:
        if x == "-t":
            generateTest = True
        else:
            className = x
    
    classNameUpper = camelCaseUpper(className)
    hFileName = className + ".h"
    cppFileName = className + ".cpp"
    testFileName = className + "Test.cpp"
    
    hFileContents = hFileTemplate.replace("$className$", className)
    hFileContents = hFileContents.replace("$CLASS_NAME$", classNameUpper)
    cppFileContents = cppFileTemplate.replace("$className$", className)
    testFileContents = testFileTemplate.replace("$className$", className)

    print("creatingFile:", os.getcwd() + "/" + hFileName)
    hFile = open(hFileName, "w")
    hFile.write(hFileContents)
    hFile.close()

    print("creatingFile:", os.getcwd() + "/" + cppFileName)
    cppFile = open(cppFileName, "w")
    cppFile.write(cppFileContents)
    cppFile.close()

    if generateTest:
        print("creatingFile:", os.getcwd() + "/" + testFileName)
        testFile = open(testFileName, "w")    
        testFile.write(testFileContents)    
        testFile.close()


main()
