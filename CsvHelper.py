import csv

class CsvReader:

    def readCSV(self, filePath):
        data = []
        with open(filePath, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)

        return data
