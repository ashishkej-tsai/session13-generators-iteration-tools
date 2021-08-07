from collections import namedtuple
import csv
from itertools import islice
import datetime

class Violations:
    def __init__(self, file_name):
        self.fname = file_name

    def __iter__(self):
        return Violations.gen_namedtuples(self.fname)

    @staticmethod
    def gen_namedtuples(fname):
        with open(fname) as f:
            rows = csv.reader(f, delimiter=',')
            first_row = list(next(rows))
            field_names = [x.replace(" ", "_") for x in first_row]
            named_tuple = namedtuple('Violations', field_names)
            for row in rows:
                row[0] = int(row[0])
                row[5] = int(row[5])
                row[4] = datetime.datetime.strptime(row[4], "%m/%d/%Y").date()
                yield named_tuple(*row)


rows = Violations('nyc_parking_tickets_extract-1.csv')
for row in islice(rows, 5):
    print(row)

def count_violations_by_make():
    violations_count = {}
    rows = Violations('nyc_parking_tickets_extract-1.csv')
    for row in rows:
        if row.Vehicle_Make in violations_count:
            violations_count[row.Vehicle_Make] += 1
        else:
            violations_count[row.Vehicle_Make] = 1
    return violations_count

counts = count_violations_by_make()
print(counts)
