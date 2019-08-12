''' before running this program make sure openpyxl is installed 
how to install pip in fedora(install as root user) 
# yum install python-pip
# yum install epel-release(not mandatory)
# pip install openpyxl 
https://www.geeksforgeeks.org/python-writing-excel-file-using-openpyxl-module/'''

import openpyxl as excel
wb = excel.load_workbook('example.xlsx')
print(type(wb))
print(wb.get_sheet_names())
sheet = wb.get_sheet_by_name(u'Sheet1')
sheet['A1'] = 'Hello world!'
print(sheet['A1'].value)
~
