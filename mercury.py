'''

mercury.py

This object's role in the simulation is to record/report events.
This object will handle all reporting/output from the simulation.
'''

import csv

class Mercury(object):

    def __init__(self, output_file_path = None):
        if(output_file_path != None):
            self.csv_file = open(output_file_path, "w")
            self.csv = csv.writer(self.csv_file, lineterminator='\n')
        else:
            self.csv_file = False
            self.csv = False
        print("Mercury Online.")

    def record_row(self, row = ['Default'])
        csv.writerow(row)

    def vale():
        self.csv_file.close()

def main():
    print("You are in a maze of little twisty passages, all alike")

if __name__ == "__main__":
    main()