# Python program to fix up the Chase bad QFX export FITID=NONE
# hleofxquotes@gmail.com
# Usage:
# python fixChaseFitidNone.py -i Checking1.qfx -o out.qfx
#
from __future__ import print_function   # If code has to work in Python 2 and 3!

import sys, getopt
import hashlib

def fixTransaction(transaction, fitid):
  if fitid == None:
    # don't need to fix up
    return transaction

  #hashObject = hashlib.md5(b'Hello World')
  longString = ""
  for item in transaction:
    longString += item
  # this is the new value for FITID
  # an MD5 hash of all the transaction items
  hexString= hashlib.md5(longString.encode()).hexdigest()
  # print(hexString)

  # now that we have a new FITID
  # sub back in the new FITID
  newTransaction = []
  for item in transaction:
    if item == '<FITID>NONE':
      item = '<FITID>' + hexString
    newTransaction.append(item)
  transaction = newTransaction

  return transaction

def fixFile(inputFile, outputFile):
  file = open(inputFile, "r")
  print ('> Reading from', inputFile)
  ofile = open(outputFile, "w")
  print ('< Writing to', outputFile)

  transaction = []
  fitid = None
  for line in file:
    #print (line)
    line = line.strip()

    if line == '<STMTTRN>':
#<STMTTRN>
      # start of transaction
      #print (line)

      # reset
      transaction = []
      fitid = None

      transaction.append(line)
    elif line == '</STMTTRN>':
#</STMTTRN> 
      # end of transaction
      #print (line)
      transaction.append(line)

      # fix up current transaction
      transaction = fixTransaction(transaction, fitid)
      for item in transaction:
        # Every thing else, write out as-id
        #print(item)
        ofile.write(item + "\n")

      # reset
      transaction = []
      fitid = None
    elif line == '<FITID>NONE':
      fitid = line
      transaction.append(line)
    else:
      if len(transaction) > 0:
        # in transaction
        transaction.append(line)
      else:
        # Everything else, write out as-is
        #print(line)
        ofile.write(line + "\n")

#<TRNTYPE>DEBIT
#<DTPOSTED>20190204120000[0:GMT]
#<TRNAMT>-11.95
#<FITID>NONE
#<NAME>SAFEWAY #2948

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

  fixFile(inputFile, outputFile)

if __name__ == "__main__":
  main(sys.argv[1:])

