import csv
import io

class CSVUtil():

    def __init__(self):
        pass

    def saveAsCSV(self, output_name, structure, header = True):
        print 'Saving %s as a csv file...' % (output_name)
        writer = csv.writer(open(output_name, 'wb'))
        writer.writerows(structure)
        print 'Done!'

    def openCSV(self, file_name):

        with open(file_name, 'rb') as csvfile:
            print 'Getting %s as a 2 dimensional array...' % file_name
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

            result = []
            for row in spamreader: result.append(row)
            print 'Done!'
            return result
