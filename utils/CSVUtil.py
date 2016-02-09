import csv
import io

class CSVUtil():

    def __init__(self):
        pass

    def saveAsCSV(self, output_name, structure, header = True):
        writer = csv.writer(open(output_name, 'wb'))
        writer.writerows(structure)
