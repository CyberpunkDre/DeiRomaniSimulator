'''

mercury.py

This object's role in the simulation is to record/report events.
This object will handle all reporting/output from the simulation.
'''

import csv

class Mercury(object):

    file_dict = {}

    def __init__(self):
        print("Mercury Online.")

    def salve(self, file_name, target_dir = '', file_type = '.txt'):
        setattr(self, file_name)
        self.file_name = open(target_dir + file_name + file_type, 'w')
        self.file_dict[file_name] = self.file_name
        
    def record(self, file_name, write_string, newline = r"\n"):
        try:
            getattr(self, file_name).write(write_string + newline)
        except(AttributeError):
            print("%s not in Mercury's file list: %s" % (file_name, self.file_dict.keys() ))

    def record_row(self, file_name, write_list, separator = ',', newline = r"\n"):
        single_string = ''
        for item in write_list:
            single_string += item + separator
        self.record(file_name, single_string, newline)

    def vale(self, file_name):
        try:
            del self.file_dict[file_name]
            getattr(self, file_name).close()
            delattr(self, file_name)
        except(KeyError):
            print("%s not in Mercury's dictionary of files: %s" % (self.file_dict.keys() ))
        except(AttributeError):
            print("%s not in Mercury's file list: %s" % (file_name, self.file_dict.keys() ))
    
    def valete(self):
        for file_name in self.file_dict.keys():
            self.vale(file_name)