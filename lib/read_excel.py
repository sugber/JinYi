import xlrd

def excel_to_data(data_file,sheet):
    data_list = []
    sh = xlrd.open_workbook(data_file)
    sh = sh.sheet_by_name(sheet)
    wb = sh.row_values(0)
    for i in range(1, sh.nrows):
        d = dict(zip(wb, sh.row_values(i)))
        data_list.append(d)
    return data_list

def get_to_case(data_list,case_name):
    for case in data_list:
        if case_name == case["case_name"]:
            return case

if __name__ == '__main__':
    data_list = excel_to_data(r'C:\Users\dell\PycharmProjects\JinYi\data\TestData.xlsx','TestWareHouse')
    case = get_to_case(data_list,'test_1_token_1')
    print(case)