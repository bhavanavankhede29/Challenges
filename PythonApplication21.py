import pandas as pd 
import os
import datetime
import shutil
import csv

class loader (object) :
    # constructor
    def __init__(self,*args):
        if args[0].endswith('.csv'):
            self.in_filename = args[0]
            # reverse filename 
            self.out_filename ="Reverse-Copy-"+str(datetime.date.today())+"-"+self.in_filename
            print('Rerse data filename :-',self.out_filename)
            #copy of filename
            self.out_filename_copy= "Copy-"+str(datetime.date.today())+"-"+self.in_filename
            print('copy of file', self.out_filename_copy)
        else :
            raise Exception('Incorrect file format')

        # function to load data 
    def load(self) :
        try :
            # checking if file exists
            if os.path.isfile(self.in_filename) :
                with open(self.in_filename) as csvFile :
                    reader = csv.reader(csvFile)
                    data = [row for row in reader]

                    # create copy of file
                shutil.copy(self.in_filename, self.out_filename_copy)
                # reverse the colunms of file
                with open(self.out_filename, 'w+', newline='') as csvFileW:
                    lines = csv.writer(csvFileW)
                    for row in data:
                        lines.writerow(row[::-1])
                    csvFileW.close()
            else :
                raise()
        except :
            print('Please check if file exists...')
#main function 
def main () :
        in_filename = input('Enter input file name :- ')
        obj = loader(in_filename)
        obj.load()


if __name__ =="__main__" :
    main()