#!/usr/bin/env python
import os
import argparse
import pprint
import csv

def main():
  # Parse User Arguments
  parser = argparse.ArgumentParser(description='This is a script to parse CLI output')
  parser.add_argument('-i','--input', help='Input file name',required=True)
  args = parser.parse_args()
  log_file = args.input
  print ("> input_file: %s" % log_file)

  # Read File's
  file_data = load_file(log_file)    #log output
  file_data = file_data.split("\n")

  # Parse Data
  session_list = []

  for line in file_data:
      if '-->' in line:
          line = line.split()
          new_list = [line[0], line[1], line[3][0:-1], line[5][0:-1], line[6], line[7][0:-1], line[8], line[9]]
          session_list.append(new_list)

  # Print Output to Terminal
  for line in session_list:
      print(",".join(line))

  # Write Output to CSV FIle
  write_csv(session_list)

def load_file(filename,verbose=False):
  # Load File as List
  try:
    f =open(filename,'r')
    if verbose == True:
      print("*** File '%s' OPENED! ***" % filename)
    file_data = f.read()
    f.close()
    return file_data
  except IOError as e:
    error="!!! I/O error({0}): {1} !!!".format(e.errno, e.strerror)
    print (error)
    exit()

def write_csv(input_list):
  #print(input_list)
  with open ("output.csv",'w') as resultFile:
      wr = csv.writer(resultFile)
      for line in input_list:
          #print(line)
          wr.writerow(line)

if __name__ == '__main__':
     main()
