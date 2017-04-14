import openpyxl

wb = openpyxl.load_workbook('block.list.new.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

for i in range(0, 100):
    a = input('请输入内容：')
    z = 0
    for line in open('queryblock.cs.keyword.txt', 'r', encoding='utf-8'):
        block = line.split('\t')[0]
        z += 1
        if block in a:
            print(block + ' %s' % z)