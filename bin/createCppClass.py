#!/usr/bin/env python2

""" Tool to create new class. """

import sys
import os
import string


hFileTemplate = """#ifndef __$CLASS_NAME$_H
#define __$CLASS_NAME$_H

class $className$
{
public:
	$className$();
	~$className$();

protected:
};

#endif
"""

cppFileTemplate = """
#include <$className$.h>

$className$::$className$()
{
}

$className$::~$className$()
{
}

"""

testFileTemplate = """
#include <$className$.h>
#include <iostream>
#include <stdlib.h>
using namespace std;

void fail()
{
	cout << "TEST_FAILED\\n";
	exit(1);
}

void test_$className$()
{
	$className$ x;
	cout << "TEST_PASSED\\n";
}

int main(int argc, char *argv[])
{
	test_$className$();
	return 0;
}
"""

def main():

    if len(sys.argv) != 2:
        print("ussage: createClass.py <class_name>")
        sys.exit(1)

    className = sys.argv[1]
    hFileName = className + ".h"
    cppFileName = className + ".cpp"
    testFileName = className + "Test.cpp"
    
    hFileContents = hFileTemplate.replace("$className$", className)
    hFileContents = hFileContents.replace("$CLASS_NAME$", className.upper())
    cppFileContents = cppFileTemplate.replace("$className$", className)
    testFileContents = testFileTemplate.replace("$className$", className)

    print(hFileName, cppFileName)

    hFile = open(hFileName, "w")
    cppFile = open(cppFileName, "w")
    testFile = open(testFileName, "w")
    
    hFile.write(hFileContents)
    cppFile.write(cppFileContents)
    testFile.write(testFileContents)
    
    hFile.close()
    cppFile.close()
    testFile.close()

main()

