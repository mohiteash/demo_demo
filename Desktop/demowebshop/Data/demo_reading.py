import xlrd
xlrd.xlsx.ensure_elementtree_imported(False,None)
xlrd.xlsx.Element_has_iter=True
path = r"C:\Users\Mohite's\PycharmProjects\pythonProject1_demowebshop\exceldemo\demo_exl.xlsx"

def read_locators():
    workbook = xlrd.open_workbook(path)
    worksheet = workbook.sheet_by_name("demo_web_shop")
    rows = worksheet.nrows
    d = {}

    for i in range(rows):
        row = worksheet.row_values(i)
        d[row[0]] = (row[1], row[2])

    return d


