#!/bin/bash

usage()
{
    echo "usage:${0} (python-project-name)"
    exit
}

[ $# -ne 1 ]&& usage
[ -e "$1" ]&& {
    echo "${1} is exist";
    exit;
}

mkdir ${1}
pro_name=`echo ${1}|tr 'A-Z' 'a-z'`

mkdir ${1}/{bin,conf,lib,doc,${pro_name}}
touch ${1}/bin/__init__.py
touch ${1}/lib/__init__.py
touch ${1}/doc/__init__.py
touch ${1}/conf/__init__.py
touch ${1}/${pro_name}/__init__.py
touch ${1}/setup.py
touch ${1}/requirements.txt
touch ${1}/README


this_year=`date +%Y`
cat <<EOF >${1}/LICENSE
MIT License

Copyright (c) ${this_year} xiongzhibiao

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

EOF




cat <<EOF >./${1}/${pro_name}/main.py
#!/usr/bin/env python
# encoding: utf-8

import os
import sys
pro_path = (os.path.abspath('./../'))
sys.path.append(pro_path)

if __name__ == "__main__":
    print (sys.path)

EOF
