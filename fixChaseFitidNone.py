# Python program to fix up the Chase bad QFX export FITID=NONE
# hleofxquotes@gmail.com
# Usage:
# python fixChaseFitidNone.py -i Checking1.qfx -o out.qfx
#
from __future__ import print_function   # If code has to work in Python 2 and 3!

import sys, getopt
import hashlib

def usage():
  print ('fixChaseFitidNone.py -i <inputFile> -o <outputFile>')

def main(argv):
  inputFile = ''
  outputFile = ''

  try:
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
  except getopt.GetoptError:
    usage()
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      usage()
      sys.exit()
    elif opt in ("-i", "--ifile"):
      inputFile = arg
    elif opt in ("-o", "--ofile"):
      outputFile = arg

  if not inputFile:
    usage()
    sys.exit(2)
  if not outputFile:
    usage()
    sys.exit(2)

  file = open(inputFile, "r")
  print ('> Reading from', inputFile)
  ofile = open(outputFile, "w")
  print ('< Writing to', outputFile)

  inTransaction = False
  for line in file:
    line = line.strip()

    if line == '<STMTTRN>':
      inTransaction = True
      transaction = []
      longString = ""

    if inTransaction:
        transaction.append(line)
        longString += item
    else:
        ofile.write(line + "\n")

    if line == '</STMTTRN>':
      inTransaction = False

      for item in fixTransaction(transaction):
        if item == '<FITID>NONE':
          item = '<FITID>' + hashlib.md5(longString.encode()).hexdigest()
        ofile.write(item + "\n")


if __name__ == "__main__":
  main(sys.argv[1:])

