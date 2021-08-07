
# EPAi Session13 Generators \& Iteration Tools
Assignment to check our knowledge of Generators and Iteration tools.

## Goal 1
Create a lazy iterator that will return a named tuple of the data in each row. The data types should be appropriate - i.e. if the column is a date, you should be storing dates in the named tuple, if the field is an integer, then it should be stored as an integer, etc.

Violations(Summons_Number=4006535600, Plate_ID='N203399C', Registration_State='NY', Plate_Type='OMT', Issue_Date=datetime.date(2016, 10, 19), Violation_Code=5, Vehicle_Body_Type='SUBN', Vehicle_Make='FORD', Violation_Description='BUS LANE VIOLATION')

## Goal 2
Calculate the number of violations by car make.

{'BMW': 34, 'CHEVR': 76, 'DODGE': 45, 'FORD': 104, 'FRUEH': 44, 'HONDA': 106, 'LINCO': 12, 'TOYOT': 112, 'CADIL': 9, 'CHRYS': 12, 'FIR': 1, 'GMC': 35, 'HYUND': 35, 'JAGUA': 3, 'JEEP': 22, 'LEXUS': 26, 'ME/BE': 38, 'MERCU': 4, 'MITSU': 11, 'NISSA': 70, 'HIN': 6, 'NS/OT': 18, 'WORKH': 2, 'ACURA': 12, 'AUDI': 12, 'INTER': 25, 'ISUZU': 10, 'KENWO': 5, 'KIA': 8, 'OLDSM': 1, 'SUBAR': 18, 'VOLVO': 12, 'SATUR': 2, 'SMART': 3, 'INFIN': 13, 'PETER': 1, '': 5, 'CITRO': 1, 'ROVER': 5, 'BUICK': 5, 'GEO': 1, 'MAZDA': 5, 'PORSC': 3, 'VOLKS': 8, 'YAMAH': 1, 'BSA': 1, 'MINI': 1, 'PONTI': 1, 'SPRI': 1, 'PLYMO': 1, 'SCION': 2, 'UPS': 1, 'FIAT': 1, 'UD': 1, 'UTILI': 1, 'GMCQ': 1, 'SAAB': 2, 'HINO': 2, 'STAR': 1, 'AM/T': 1, 'MI/F': 1}

Note:
Try to use lazy evaluation as much as possible - it may not always be possible though! That's OK, as long as it's kept to a minimum.

No Test Cases
