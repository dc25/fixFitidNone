#! /usr/bin/python 
# Python program to fix up the Chase bad QFX export FITID=NONE
# modified version of : fixChaseFitidNone.py by hleofxquotes@gmail.com
# (see https://social.microsoft.com/Forums/mvpforum/en-US/f9a4fa77-fe71-4eed-a66e-c828572ab911/fixchasefitidnonepy-python-script-to-fix-up-chase-ltfitidgtnone?forum=money)
# python fixChaseFitidNone.py Checking1.qfx 
#
from __future__ import print_function   # If code has to work in Python 2 and 3!

import sys
import fileinput
from shutil import copyfile
import hashlib

def main(argv):
  qfxfile=sys.argv[1]
  copyfile(qfxfile, qfxfile+".original")

  inTransaction = False
  for line in fileinput.input(qfxfile, inplace = True):
    line = line.strip()

    if line == '<STMTTRN>':
      inTransaction = True
      transaction = []
      longString = ""

    if inTransaction:
        transaction.append(line)
        longString += line

        if line == '</STMTTRN>':
          inTransaction = False

          for item in transaction:
            if item == '<FITID>NONE':
              item = '<FITID>' + hashlib.md5(longString.encode()).hexdigest()
            print(item)
    else:
        print(line)

if __name__ == "__main__":
  main(sys.argv[1:])
